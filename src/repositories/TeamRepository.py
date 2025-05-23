from typing import List, Optional
from src.entities.Team import Team
from src.entities.Base import db


def list_all() -> List[Team]:
    return db.session.query(Team).all()


def get(team_id: int) -> Optional[Team]:
    return db.session.query(Team).get(team_id)


def add(
    name: str,
    logo_url: str = None,
    base_country: str = None,
    principal: str = None,
    founded_year: int = None,
) -> Team:
    team = Team(
        name=name,
        logo_url=logo_url,
        base_country=base_country,
        principal=principal,
        founded_year=founded_year,
    )
    db.session.add(team)
    db.session.commit()
    return team


def update(team_id: int, **fields) -> Optional[Team]:
    team = get(team_id)
    if not team:
        return None
    for k, v in fields.items():
        setattr(team, k, v)
    db.session.commit()
    return team


def delete(team_id: int) -> bool:
    team = get(team_id)
    if not team:
        return False
    db.session.delete(team)
    db.session.commit()
    return True
