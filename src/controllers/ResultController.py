from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.ResultService import (
    getResults,
    getResult,
    addResult,
    updateResult,
    deleteResult,
)

# ---------- Schemas ---------- #
class ResultResponseSchema(Schema):
    id = fields.Int()
    race_id = fields.Int()
    team_id = fields.Int()
    driver_id = fields.Int()
    position = fields.Int()
    points = fields.Int()
    fastest_lap = fields.Bool()


class ResultRequestSchema(Schema):
    race_id = fields.Int(required=True)
    team_id = fields.Int(required=True)
    driver_id = fields.Int(required=True)
    position = fields.Int(required=True)
    points = fields.Int(required=True)
    fastest_lap = fields.Bool()

    @validates("position")
    def validate_position(self, value: int):
        if value < 1 or value > 20:
            raise ValidationError("position must be between 1 and 20")

    @validates("points")
    def validate_points(self, value: int):
        if value < 0 or value > 25:
            raise ValidationError("points must be between 0 and 25")


# ---------- Recursos ---------- #
class ResultItem(MethodResource, Resource):
    @marshal_with(ResultResponseSchema)
    def get(self, result_id: int):
        try:
            res = getResult(result_id)
            if not res:
                abort(404, message="Resource not found")
            return res, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(ResultRequestSchema, location=("form"))
    @marshal_with(ResultResponseSchema)
    def put(self, result_id: int, **kwargs):
        try:
            res = updateResult(result_id, kwargs)
            if not res:
                abort(404, message="Resource not found")
            return res, 200
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, result_id: int):
        try:
            deleted = deleteResult(result_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class ResultList(MethodResource, Resource):
    @marshal_with(ResultResponseSchema(many=True))
    def get(self):
        try:
            return getResults(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(ResultRequestSchema, location=("form"))
    @marshal_with(ResultResponseSchema)
    def post(self, **kwargs):
        try:
            res = addResult(**kwargs)
            return res, 201
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")
