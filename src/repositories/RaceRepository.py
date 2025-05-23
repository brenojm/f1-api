from typing import List, Optional
from datetime import date
from src.entities.Race import Race
from src.entities.Base import db


def list_all() -> List[Race]:
    return db.session.query(Race).all()


def get(race_id: int) -> Optional[Race]:
    return db.session.query(Race).get(race_id)


def add(
    name: str,
    race_date: date,
    season_id: int,
    circuit_id: int,
    laps: int = None,
    weather: str = None,
) -> Race:
    race = Race(
        name=name,
        race_date=race_date,
        season_id=season_id,
        circuit_id=circuit_id,
        laps=laps,
        weather=weather,
    )
    db.session.add(race)
    db.session.commit()
    return race


def update(race_id: int, **fields) -> Optional[Race]:
    race = get(race_id)
    if not race:
        return None
    for k, v in fields.items():
        setattr(race, k, v)
    db.session.commit()
    return race


def delete(race_id: int) -> bool:
    race = get(race_id)
    if not race:
        return False
    db.session.delete(race)
    db.session.commit()
    return True
