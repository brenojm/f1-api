from flask_restful import Resource, abort
from flask_apispec import marshal_with, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, ValidationError, fields, validates
from sqlalchemy.exc import IntegrityError, OperationalError

from src.services.SeasonService import (
    getSeasons,
    getSeason,
    addSeason,
    updateSeason,
    deleteSeason,
    teamStandings,
    driverStandings
)

# ---------- Schemas ---------- #
class SeasonResponseSchema(Schema):
    id = fields.Int()
    year = fields.Int()
    start_date = fields.Date()
    description = fields.Str(allow_none=True)


class SeasonRequestSchema(Schema):
    year = fields.Int(required=True)
    start_date = fields.Date(required=True)
    description = fields.Str()

    @validates("year")
    def validate_year(self, value: int):
        if value < 1950:
            raise ValidationError("year must be 1950 or greater")

class DriverStandingSchema(Schema):
    driver_id = fields.Int()
    full_name = fields.Str()
    points = fields.Int()

class TeamStandingSchema(Schema):
    team_id = fields.Int()
    name = fields.Str()
    points = fields.Int()


# ---------- Recursos ---------- #
class SeasonItem(MethodResource, Resource):
    @marshal_with(SeasonResponseSchema)
    def get(self, season_id: int):
        try:
            season = getSeason(season_id)
            if not season:
                abort(404, message="Resource not found")
            return season, 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(SeasonRequestSchema, location=("form"))
    @marshal_with(SeasonResponseSchema)
    def put(self, season_id: int, **kwargs):
        try:
            season = updateSeason(season_id, kwargs)
            if not season:
                abort(404, message="Resource not found")
            return season, 200
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

    def delete(self, season_id: int):
        try:
            deleted = deleteSeason(season_id)
            if not deleted:
                abort(404, message="Resource not found")
            return "", 204
        except OperationalError:
            abort(500, message="Internal Server Error")


class SeasonList(MethodResource, Resource):
    @marshal_with(SeasonResponseSchema(many=True))
    def get(self):
        try:
            return getSeasons(), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

    @use_kwargs(SeasonRequestSchema, location=("form"))
    @marshal_with(SeasonResponseSchema)
    def post(self, **kwargs):
        try:
            season = addSeason(**kwargs)
            return season, 201
        except (IntegrityError, ValidationError) as err:
            abort(400, message=str(err))
        except OperationalError:
            abort(500, message="Internal Server Error")

class SeasonDriverStandings(MethodResource, Resource):
    @marshal_with(DriverStandingSchema(many=True))
    def get(self, season_id: int):
        try:
            return driverStandings(season_id), 200
        except OperationalError:
            abort(500, message="Internal Server Error")

class SeasonTeamStandings(MethodResource, Resource):
    @marshal_with(TeamStandingSchema(many=True))
    def get(self, season_id: int):
        try:
            return teamStandings(season_id), 200
        except OperationalError:
            abort(500, message="Internal Server Error")