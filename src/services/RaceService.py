from typing import List, Optional
from datetime import date
from marshmallow import ValidationError

from src.entities.Race import Race
from src.repositories.RaceRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)
from src.repositories.SeasonRepository import get as get_season


# ---------- Funções públicas ---------- #
def getRaces() -> List[Race]:
    return list_all()


def getRace(race_id: int) -> Optional[Race]:
    return get(race_id)


def addRace(
    name: str,
    race_date: date,
    season_id: int,
    circuit_id: int,
    laps: int = None,
    weather: str = None,
) -> Race:
    _validate_common(name, race_date, season_id, laps, weather)
    return add(
        name=name,
        race_date=race_date,
        season_id=season_id,
        circuit_id=circuit_id,
        laps=laps,
        weather=weather,
    )


def updateRace(race_id: int, data: dict) -> Optional[Race]:
    race = get(race_id)
    if not race:
        return None

    name = data.get("name", race.name)
    race_date = data.get("race_date", race.race_date)
    laps = data.get("laps", race.laps)
    weather = data.get("weather", race.weather)
    season_id = race.season_id  # temporada não muda

    _validate_common(name, race_date, season_id, laps, weather)
    return update(race_id, **data)


def deleteRace(race_id: int) -> bool:
    return delete(race_id)


# ---------- Validações privadas ---------- #
def _validate_common(
    name: str,
    race_date: date,
    season_id: int,
    laps: int,
    weather: str,
):
    if not name:
        raise ValidationError("name must not be empty")

    season = get_season(season_id)
    if race_date < season.start_date:
        raise ValidationError("race_date cannot be before season start date")

    if laps is not None and laps <= 0:
        raise ValidationError("laps must be positive")

    if weather and weather not in ("Dry", "Wet", "Mixed"):
        raise ValidationError("weather must be Dry, Wet or Mixed")
