import re

from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.DriverService import (
    getDrivers,
    getDriver,
    addDriver,
    updateDriver,
    deleteDriver,
)

# ---------- Schemas ---------- #
class DriverResponseSchema(Schema):
    id = fields.Int()
    full_name = fields.Str()
    nationality = fields.Str(allow_none=True)
    date_of_birth = fields.Date(allow_none=True)


class DriverRequestSchema(Schema):
    full_name = fields.Str(required=True)
    nationality = fields.Str()
    date_of_birth = fields.Date()

    @validates("full_name")
    def validate_name(self, value: str):
        if not re.match(r"^[a-zA-Z0-9_\s]+$", value):
            raise ValidationError(
                "Value must contain only alphanumeric characters, spaces or underscores."
            )


# ---------- Recursos ---------- #
class DriverItem(MethodResource, Resource):
    @marshal_with(DriverResponseSchema)
    def get(self, driver_id: int):
        try:
            driver = getDriver(driver_id)
            if not driver:
                abort(404, message="Resource not found")
            return driver, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(DriverRequestSchema, location=("form"))
    @marshal_with(DriverResponseSchema)
    def put(self, driver_id: int, **kwargs):
        try:
            driver = updateDriver(driver_id, kwargs)
            if not driver:
                abort(404, message="Resource not found")
            return driver, 200
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError:
            abort(500, message=str(err.__context__))

    def delete(self, driver_id: int):
        try:
            deleted = deleteDriver(driver_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class DriverList(MethodResource, Resource):
    @marshal_with(DriverResponseSchema(many=True))
    def get(self):
        try:
            return getDrivers(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(DriverRequestSchema, location=("form"))
    @marshal_with(DriverResponseSchema)
    def post(self, **kwargs):
        try:
            driver = addDriver(**kwargs)
            return driver, 201
        except IntegrityError as err:
            abort(500, message=str(err.__context__))
        except OperationalError as err:
            abort(500, message=str(err.__context__))
