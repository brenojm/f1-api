from typing import List, Optional
from datetime import date
from src.entities.Season import Season
from src.entities.Base import db


def list_all() -> List[Season]:
    return db.session.query(Season).all()


def get(season_id: int) -> Optional[Season]:
    return db.session.query(Season).get(season_id)


def add(year: int, start_date: date, description: str = None) -> Season:
    season = Season(year=year, start_date=start_date, description=description)
    db.session.add(season)
    db.session.commit()
    return season


def update(season_id: int, **fields) -> Optional[Season]:
    season = get(season_id)
    if not season:
        return None
    for k, v in fields.items():
        setattr(season, k, v)
    db.session.commit()
    return season


def delete(season_id: int) -> bool:
    season = get(season_id)
    if not season:
        return False
    db.session.delete(season)
    db.session.commit()
    return True
