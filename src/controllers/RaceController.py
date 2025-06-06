import re

from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.RaceService import (
    getRaces,
    getRace,
    addRace,
    updateRace,
    deleteRace,
)

# ---------- Schemas ---------- #
class RaceResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    race_date = fields.Date()
    season_id = fields.Int()
    circuit_id = fields.Int()
    laps = fields.Int(allow_none=True)
    weather = fields.Str(allow_none=True)


class RaceRequestSchema(Schema):
    name = fields.Str(required=True)
    race_date = fields.Date(required=True)
    season_id = fields.Int(required=True)
    circuit_id = fields.Int(required=True)
    laps = fields.Int()
    weather = fields.Str()

    @validates("name")
    def validate_name(self, value: str):
        if not re.match(r"^[a-zA-Z0-9_\s]+$", value):
            raise ValidationError("Invalid race name")

    @validates("laps")
    def validate_laps(self, value: int):
        if value is not None and value <= 0:
            raise ValidationError("laps must be positive")

    @validates("weather")
    def validate_weather(self, value: str):
        if value and value not in ("Dry", "Wet", "Mixed"):
            raise ValidationError("weather must be Dry, Wet or Mixed")


# ---------- Recursos ---------- #
class RaceItem(MethodResource, Resource):
    @marshal_with(RaceResponseSchema)
    def get(self, race_id: int):
        try:
            race = getRace(race_id)
            if not race:
                abort(404, message="Resource not found")
            return race, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(RaceRequestSchema, location=("form"))
    @marshal_with(RaceResponseSchema)
    def put(self, race_id: int, **kwargs):
        try:
            race = updateRace(race_id, kwargs)
            if not race:
                abort(404, message="Resource not found")
            return race, 200
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, race_id: int):
        try:
            deleted = deleteRace(race_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class RaceList(MethodResource, Resource):
    @marshal_with(RaceResponseSchema(many=True))
    def get(self):
        try:
            return getRaces(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(RaceRequestSchema, location=("form"))
    @marshal_with(RaceResponseSchema)
    def post(self, **kwargs):
        try:
            race = addRace(**kwargs)
            return race, 201
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")
