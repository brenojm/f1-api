from typing import List, Optional
from marshmallow import ValidationError

from src.entities.Result import Result
from src.repositories.ResultRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)
from src.repositories.RaceRepository import get as get_race
from src.repositories.TeamRepository import get as get_team
from src.repositories.DriverRepository import get as get_driver


# ---------- Validações internas ---------- #
def _validate_unique_race_driver(race_id: int, driver_id: int):
    if any(r.race_id == race_id and r.driver_id == driver_id for r in list_all()):
        raise ValidationError("this driver already has a result for this race")


def _validate_max_two_per_team(race_id: int, team_id: int, driver_id: int):
    driver_set = {
        r.driver_id
        for r in list_all()
        if r.race_id == race_id and r.team_id == team_id
    }
    driver_set.add(driver_id)
    if len(driver_set) > 2:
        raise ValidationError("team already has two drivers in this race")


def _validate_position_points(position: int, points: int):
    if position < 1 or position > 20:
        raise ValidationError("position must be between 1 and 20")
    if points < 0 or points > 25:
        raise ValidationError("points must be between 0 and 25")


# ---------- Funções públicas ---------- #
def getResults() -> List[Result]:
    return list_all()

def getResultsByDriverId(driver_id: int) -> List[Result]:
    return [r for r in list_all() if r.driver_id == driver_id]


def getResult(result_id: int) -> Optional[Result]:
    return get(result_id)


def addResult(
    race_id: int,
    team_id: int,
    driver_id: int,
    position: int,
    points: int,
    fastest_lap: bool = False,
) -> Result:
    # existência das FK
    if not get_race(race_id):
        raise ValidationError("race not found")
    if not get_team(team_id):
        raise ValidationError("team not found")
    if not get_driver(driver_id):
        raise ValidationError("driver not found")

    _validate_unique_race_driver(race_id, driver_id)
    _validate_max_two_per_team(race_id, team_id, driver_id)
    _validate_position_points(position, points)

    return add(
        race_id=race_id,
        team_id=team_id,
        driver_id=driver_id,
        position=position,
        points=points,
        fastest_lap=fastest_lap,
    )


def updateResult(result_id: int, data: dict) -> Optional[Result]:
    res = get(result_id)
    if not res:
        return None

    position = data.get("position", res.position)
    points = data.get("points", res.points)

    _validate_position_points(position, points)

    # se driver ou team forem alterados, verificar regras 1 e 8 outra vez
    new_driver = data.get("driver_id", res.driver_id)
    new_team = data.get("team_id", res.team_id)
    new_race = res.race_id

    if new_driver != res.driver_id:
        _validate_unique_race_driver(new_race, new_driver)

    if new_team != res.team_id or new_driver != res.driver_id:
        _validate_max_two_per_team(new_race, new_team, new_driver)

    return update(result_id, **data)


def deleteResult(result_id: int) -> bool:
    return delete(result_id)
