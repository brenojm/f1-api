from typing import List, Optional
from marshmallow import ValidationError

from src.entities.DriverContract import DriverContract
from src.repositories.DriverContractRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)
from src.repositories.SeasonRepository import get as get_season
from src.repositories.TeamRepository import get as get_team
from src.repositories.DriverRepository import get as get_driver


# ---------- Helpers internos ---------- #
def _driver_already_contracted(season_id: int, driver_id: int) -> bool:
    return any(
        c.driver_id == driver_id and c.season_id == season_id
        for c in list_all()
    )


def _team_contract_count(season_id: int, team_id: int) -> int:
    return len(
        [c for c in list_all() if c.season_id == season_id and c.team_id == team_id]
    )


# ---------- Funções públicas ---------- #
def getContracts() -> List[DriverContract]:
    return list_all()


def getContract(contract_id: int) -> Optional[DriverContract]:
    return get(contract_id)


def addContract(
    season_id: int,
    team_id: int,
    driver_id: int,
    number: int,
    salary_musd: float = None,
) -> DriverContract:
    season = get_season(season_id)
    if not season:
        raise ValidationError("season not found")
    if not get_team(team_id):
        raise ValidationError("team not found")
    if not get_driver(driver_id):
        raise ValidationError("driver not found")

    
    if number < 1 or number > 99:
        raise ValidationError("number must be between 1 and 99")
    
    existing_contracts = list_all()
    for contract in existing_contracts:
        if contract.number == number and contract.season == get_season(season_id):
            raise ValidationError(f"number {number} already taken in {season.year} season")

    
    if _driver_already_contracted(season_id, driver_id):
        raise ValidationError("driver already contracted in this season")

    
    if _team_contract_count(season_id, team_id) >= 2:
        raise ValidationError("team already has two drivers in this season")

    return add(
        season_id=season_id,
        team_id=team_id,
        driver_id=driver_id,
        number=number,
        salary_musd=salary_musd,
    )


def updateContract(contract_id: int, data: dict) -> Optional[DriverContract]:
    if any(k in data for k in ("season_id", "team_id", "driver_id")):
        raise ValidationError("season_id, team_id and driver_id are immutable")

    if "number" in data:
        if data["number"] < 1 or data["number"] > 99:
            raise ValidationError("number must be between 1 and 99")

    return update(contract_id, **data)


def deleteContract(contract_id: int) -> bool:
    return delete(contract_id)
