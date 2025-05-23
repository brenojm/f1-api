from typing import List, Optional
from src.entities.Circuit import Circuit
from src.entities.Base import db


def list_all() -> List[Circuit]:
    return db.session.query(Circuit).all()


def get(circuit_id: int) -> Optional[Circuit]:
    return db.session.query(Circuit).get(circuit_id)


def add(
    name: str,
    country: str,
    image_url: str = None,
    length_km: float = None,
    map_url: str = None,
) -> Circuit:
    circuit = Circuit(
        name=name,
        country=country,
        image_url=image_url,
        length_km=length_km,
        map_url=map_url,
    )
    db.session.add(circuit)
    db.session.commit()
    return circuit


def update(circuit_id: int, **fields) -> Optional[Circuit]:
    circuit = get(circuit_id)
    if not circuit:
        return None
    for k, v in fields.items():
        setattr(circuit, k, v)
    db.session.commit()
    return circuit


def delete(circuit_id: int) -> bool:
    circuit = get(circuit_id)
    if not circuit:
        return False
    db.session.delete(circuit)
    db.session.commit()
    return True
