import re

from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.TeamService import (
    getTeams,
    getTeam,
    addTeam,
    updateTeam,
    deleteTeam,
)

# ---------- Schemas ---------- #
class TeamResponseSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    logo_url = fields.Str(allow_none=True)
    base_country = fields.Str(allow_none=True)
    principal = fields.Str(allow_none=True)
    founded_year = fields.Int(allow_none=True)


class TeamRequestSchema(Schema):
    name = fields.Str(required=True)
    logo_url = fields.Str()
    base_country = fields.Str()
    principal = fields.Str()
    founded_year = fields.Int()

    @validates("name")
    def validate_name(self, value: str):
        if not re.match(r"^[a-zA-Z0-9_\s]+$", value):
            raise ValidationError(
                "Value must contain only alphanumeric characters, spaces or underscores."
            )

    @validates("base_country")
    def validate_country(self, value: str):
        if value and len(value) != 3:
            raise ValidationError("base_country must have exactly 3 characters")


# ---------- Recursos ---------- #
class TeamItem(MethodResource, Resource):
    @marshal_with(TeamResponseSchema)
    def get(self, team_id: int):
        try:
            team = getTeam(team_id)
            if not team:
                abort(404, message="Resource not found")
            return team, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(TeamRequestSchema, location=("form"))
    @marshal_with(TeamResponseSchema)
    def put(self, team_id: int, **kwargs):
        try:
            print(kwargs)
            team = updateTeam(team_id, kwargs)
            if not team:
                abort(404, message="Resource not found")
            return team, 200
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, team_id: int):
        try:
            deleted = deleteTeam(team_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class TeamList(MethodResource, Resource):
    @marshal_with(TeamResponseSchema(many=True))
    def get(self):
        try:
            return getTeams(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(TeamRequestSchema, location=("form"))
    @marshal_with(TeamResponseSchema)
    def post(self, **kwargs):
        try:
            team = addTeam(**kwargs)
            return team, 201
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")
