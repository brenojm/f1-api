from typing import List, Optional
from src.entities.Driver import Driver
from src.entities.Base import db


def list_all() -> List[Driver]:
    return db.session.query(Driver).all()


def get(driver_id: int) -> Optional[Driver]:
    return db.session.query(Driver).get(driver_id)


def add(
    full_name: str,
    nationality: str = None,
    date_of_birth=None,
    image_url: str = None,
) -> Driver:
    driver = Driver(
        full_name=full_name,
        nationality=nationality,
        date_of_birth=date_of_birth,
        image_url=image_url,
    )
    db.session.add(driver)
    db.session.commit()
    return driver


def update(driver_id: int, **fields) -> Optional[Driver]:
    driver = get(driver_id)
    if not driver:
        return None
    for k, v in fields.items():
        setattr(driver, k, v)
    db.session.commit()
    return driver


def delete(driver_id: int) -> bool:
    driver = get(driver_id)
    if not driver:
        return False
    db.session.delete(driver)
    db.session.commit()
    return True
