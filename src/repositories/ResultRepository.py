from typing import List, Optional
from src.entities.Result import Result
from src.entities.Base import db


def list_all() -> List[Result]:
    return db.session.query(Result).all()


def get(result_id: int) -> Optional[Result]:
    return db.session.query(Result).get(result_id)


def add(
    race_id: int,
    team_id: int,
    driver_id: int,
    position: int,
    points: int,
    fastest_lap: bool = False,
) -> Result:
    result = Result(
        race_id=race_id,
        team_id=team_id,
        driver_id=driver_id,
        position=position,
        points=points,
        fastest_lap=fastest_lap,
    )
    db.session.add(result)
    db.session.commit()
    return result


def update(result_id: int, **fields) -> Optional[Result]:
    result = get(result_id)
    if not result:
        return None
    for k, v in fields.items():
        setattr(result, k, v)
    db.session.commit()
    return result


def delete(result_id: int) -> bool:
    result = get(result_id)
    if not result:
        return False
    db.session.delete(result)
    db.session.commit()
    return True
