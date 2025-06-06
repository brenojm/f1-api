from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.DriverContractService import (
    getContracts,
    getContract,
    addContract,
    updateContract,
    deleteContract,
)

# ---------- Schemas ---------- #
class ContractResponseSchema(Schema):
    id = fields.Int()
    season_id = fields.Int()
    team_id = fields.Int()
    driver_id = fields.Int()
    number = fields.Int()
    salary_musd = fields.Float(allow_none=True)


class ContractRequestSchema(Schema):
    season_id = fields.Int(required=True)
    team_id = fields.Int(required=True)
    driver_id = fields.Int(required=True)
    number = fields.Int(required=True)
    salary_musd = fields.Float()

    @validates("number")
    def validate_number(self, value: int):
        if value < 1 or value > 99:
            raise ValidationError("number must be between 1 and 99")

    @validates("salary_musd")
    def validate_salary(self, value: float):
        if value is not None and value < 0:
            raise ValidationError("salary_musd must be positive")


# ---------- Recursos ---------- #
class ContractItem(MethodResource, Resource):
    @marshal_with(ContractResponseSchema)
    def get(self, contract_id: int):
        try:
            obj = getContract(contract_id)
            if not obj:
                abort(404, message="Resource not found")
            return obj, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(ContractRequestSchema, location=("form"))
    @marshal_with(ContractResponseSchema)
    def put(self, contract_id: int, **kwargs):
        try:
            obj = updateContract(contract_id, kwargs)
            if not obj:
                abort(404, message="Resource not found")
            return obj, 200
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, contract_id: int):
        try:
            deleted = deleteContract(contract_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class ContractList(MethodResource, Resource):
    @marshal_with(ContractResponseSchema(many=True))
    def get(self):
        try:
            return getContracts(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(ContractRequestSchema, location=("form"))
    @marshal_with(ContractResponseSchema)
    def post(self, **kwargs):
        try:
            obj = addContract(**kwargs)
            return obj, 201
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")
