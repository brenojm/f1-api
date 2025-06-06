import re

from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.CircuitService import (
    getCircuits,
    getCircuit,
    addCircuit,
    updateCircuit,
    deleteCircuit,
)

# ---------- Schemas ---------- #
class CircuitResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    country = fields.Str()
    image_url = fields.Str(allow_none=True)
    length_km = fields.Float(allow_none=True)
    map_url = fields.Str(allow_none=True)


class CircuitRequestSchema(Schema):
    name = fields.Str(required=True)
    country = fields.Str(required=True)
    image_url = fields.Str()
    length_km = fields.Float()
    map_url = fields.Str()

    @validates("name")
    def validate_name(self, value: str):
        if not re.match(r"^[a-zA-Z0-9_\s]+$", value):
            raise ValidationError("Invalid circuit name")

    @validates("country")
    def validate_country(self, value: str):
        if len(value) != 3:
            raise ValidationError("country must have exactly 3 characters")

    @validates("length_km")
    def validate_length(self, value: float):
        if value is not None and value <= 0:
            raise ValidationError("length_km must be positive")


# ---------- Recursos ---------- #
class CircuitItem(MethodResource, Resource):
    @marshal_with(CircuitResponseSchema)
    def get(self, circuit_id: int):
        try:
            circuit = getCircuit(circuit_id)
            if not circuit:
                abort(404, message="Resource not found")
            return circuit, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(CircuitRequestSchema, location=("form"))
    @marshal_with(CircuitResponseSchema)
    def put(self, circuit_id: int, **kwargs):
        try:
            circuit = updateCircuit(circuit_id, kwargs)
            if not circuit:
                abort(404, message="Resource not found")
            return circuit, 200
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, circuit_id: int):
        try:
            deleted = deleteCircuit(circuit_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class CircuitList(MethodResource, Resource):
    @marshal_with(CircuitResponseSchema(many=True))
    def get(self):
        try:
            return getCircuits(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(CircuitRequestSchema, location=("form"))
    @marshal_with(CircuitResponseSchema)
    def post(self, **kwargs):
        try:
            circuit = addCircuit(**kwargs)
            return circuit, 201
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")
