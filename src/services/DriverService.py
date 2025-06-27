from typing import List, Optional
from marshmallow import ValidationError
from src.repositories.DriverRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)
from src.services.ResultService import getResultsByDriverId
from src.entities.Driver import Driver

def getDrivers() -> List[Driver]:
    return list_all()


def getDriver(driver_id: int) -> Optional[Driver]:
    return get(driver_id)

def addDriver(full_name: str, nationality: str = None, date_of_birth=None, image_url: str = None) -> Driver:
    if not full_name:
        raise ValidationError("full_name must not be empty")
    return add(full_name=full_name, nationality=nationality, date_of_birth=date_of_birth, image_url=image_url)


def updateDriver(driver_id: int, data: dict) -> Optional[Driver]:
    return update(driver_id, **data)


def deleteDriver(driver_id: int) -> bool:
    driver_to_delete = get(driver_id)
    if not driver_to_delete:
        raise ValidationError("driver not found")

    results = getResultsByDriverId(driver_id)
    if results:
        raise ValidationError(f"cannot delete driver {driver_id} as there are associated results.")
    return delete(driver_id)
