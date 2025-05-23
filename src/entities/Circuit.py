from sqlalchemy import (
    Column, Integer, String, Float, UniqueConstraint, Index, CheckConstraint
)
from sqlalchemy.orm import relationship
from .Base import Base

class Circuit(Base):
    __tablename__ = "circuits"

    id         = Column(Integer, primary_key=True)
    name       = Column(String(100), nullable=False)
    country    = Column(String(3),  nullable=False)
    image_url  = Column(String(250))
    length_km  = Column(Float)                      
    map_url    = Column(String(250))

    __table_args__ = (
        UniqueConstraint("name", "country", name="uq_circuit_name_country"),
        CheckConstraint("char_length(country)=3", name="ck_circuit_country_len"),
        CheckConstraint("length_km IS NULL OR length_km > 0", name="ck_circuit_len"),
        Index("ix_circuit_country", "country"),
    )

    races = relationship("Race", back_populates="circuit")
