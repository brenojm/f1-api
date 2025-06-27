from typing import List, Optional
from datetime import date
from marshmallow import ValidationError
from sqlalchemy import func, desc, case

from src.entities.Season import Season
from src.entities.Result import Result
from src.entities.Race import Race
from src.entities.Driver import Driver
from src.entities.Team import Team
from src.entities.Base import db
from src.repositories.SeasonRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)


# ---------- Funções públicas ---------- #
def getSeasons() -> List[Season]:
    return list_all()


def getSeason(season_id: int) -> Optional[Season]:
    return get(season_id)


def addSeason(year: int, start_date: date, description: str = None) -> Season:
    if year < 1950:
        raise ValidationError("year must be 1950 or greater")
    if start_date is None:
        raise ValidationError("start_date is required")
    return add(year=year, start_date=start_date, description=description)


def updateSeason(season_id: int, data: dict) -> Optional[Season]:
    if "year" in data and data["year"] < 1950:
        raise ValidationError("year must be 1950 or greater")
    return update(season_id, **data)


def deleteSeason(season_id: int) -> bool:
    return delete(season_id)

def driverStandings(season_id: int):
    """Retorna ranking de pilotos da temporada, incluindo 1 ponto extra para fastest_lap."""
    rows = (
        db.session.query(
            Driver.id.label("driver_id"),
            Driver.full_name,
            # Somas os pontos existentes e adiciona 1 se fastest_lap for TRUE
            (func.coalesce(func.sum(Result.points), 0) +
             func.sum(case((Result.fastest_lap == True, 1), else_=0))).label("points"),
        )
        .join(Result, Driver.id == Result.driver_id)
        .join(Race, Result.race_id == Race.id)
        .filter(Race.season_id == season_id)
        .group_by(Driver.id, Driver.full_name) # Inclua Driver.full_name no GROUP BY para evitar avisos
        .order_by(desc("points"), Driver.full_name)
        .all()
    )
    return [dict(r._mapping) for r in rows]

def teamStandings(season_id: int):
    """Retorna ranking de equipes da temporada, incluindo 1 ponto extra para fastest_lap."""
    rows = (
        db.session.query(
            Team.id.label("team_id"),
            Team.name,
            # Somas os pontos existentes e adiciona 1 se fastest_lap for TRUE para resultados da equipe
            (func.coalesce(func.sum(Result.points), 0) +
             func.sum(case((Result.fastest_lap == True, 1), else_=0))).label("points"),
        )
        .join(Result, Team.id == Result.team_id)
        .join(Race, Result.race_id == Race.id)
        .filter(Race.season_id == season_id)
        .group_by(Team.id, Team.name) # Inclua Team.name no GROUP BY para evitar avisos
        .order_by(desc("points"), Team.name)
        .all()
    )
    return [dict(r._mapping) for r in rows]
