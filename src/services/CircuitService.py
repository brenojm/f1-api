from typing import List, Optional
from marshmallow import ValidationError

from src.entities.Circuit import Circuit
from src.repositories.CircuitRepository import (
    list_all,
    get,
    add,
    update,
    delete,
)


# ---------- Funções públicas ---------- #
def getCircuits() -> List[Circuit]:
    return list_all()


def getCircuit(circuit_id: int) -> Optional[Circuit]:
    return get(circuit_id)


def addCircuit(
    name: str,
    country: str,
    image_url: str = None,
    length_km: float = None,
    map_url: str = None,
) -> Circuit:
    if not name:
        raise ValidationError("name must not be empty")
    if len(country) != 3:
        raise ValidationError("country must be ISO-3166 alpha-3 (3 chars)")
    if length_km is not None and length_km <= 0:
        raise ValidationError("length_km must be positive")
    return add(
        name=name,
        country=country,
        image_url=image_url,
        length_km=length_km,
        map_url=map_url,
    )


def updateCircuit(circuit_id: int, data: dict) -> Optional[Circuit]:
    if "name" in data and not data["name"]:
        raise ValidationError("name must not be empty")
    if "country" in data and data["country"] and len(data["country"]) != 3:
        raise ValidationError("country must be ISO-3166 alpha-3 (3 chars)")
    if "length_km" in data and data["length_km"] is not None:
        if data["length_km"] <= 0:
            raise ValidationError("length_km must be positive")
    return update(circuit_id, **data)


def deleteCircuit(circuit_id: int) -> bool:
    return delete(circuit_id)
