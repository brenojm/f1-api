from typing import List, Optional
from marshmallow import ValidationError

from src.entities.Team import Team
from src.repositories.TeamRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)


# ---------- Funções públicas ---------- #
def getTeams() -> List[Team]:
    return list_all()


def getTeam(team_id: int) -> Optional[Team]:
    return get(team_id)


def addTeam(
    name: str,
    logo_url: str = None,
    base_country: str = None,
    principal: str = None,
    founded_year: int = None,
) -> Team:
    if not name:
        raise ValidationError("name must not be empty")

    # valida ISO-3166 alpha-3
    if base_country and len(base_country) != 3:
        raise ValidationError("base_country must have exactly 3 characters")

    return add(
        name=name,
        logo_url=logo_url,
        base_country=base_country,
        principal=principal,
        founded_year=founded_year,
    )


def updateTeam(team_id: int, data: dict) -> Optional[Team]:
    if "name" in data and not data["name"]:
        raise ValidationError("name must not be empty")

    if "base_country" in data and data["base_country"]:
        if len(data["base_country"]) != 3:
            raise ValidationError("base_country must have exactly 3 characters")

    return update(team_id, **data)


def deleteTeam(team_id: int) -> bool:
    return delete(team_id)
