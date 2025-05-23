from typing import List, Optional
from src.entities.DriverContract import DriverContract
from src.entities.Base import db


def list_all() -> List[DriverContract]:
    return db.session.query(DriverContract).all()


def get(contract_id: int) -> Optional[DriverContract]:
    return db.session.query(DriverContract).get(contract_id)


def add(
    season_id: int,
    team_id: int,
    driver_id: int,
    number: int,
    salary_musd: float = None,
) -> DriverContract:
    contract = DriverContract(
        season_id=season_id,
        team_id=team_id,
        driver_id=driver_id,
        number=number,
        salary_musd=salary_musd,
    )
    db.session.add(contract)
    db.session.commit()
    return contract


def update(contract_id: int, **fields) -> Optional[DriverContract]:
    contract = get(contract_id)
    if not contract:
        return None
    for k, v in fields.items():
        setattr(contract, k, v)
    db.session.commit()
    return contract


def delete(contract_id: int) -> bool:
    contract = get(contract_id)
    if not contract:
        return False
    db.session.delete(contract)
    db.session.commit()
    return True
