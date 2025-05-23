from sqlalchemy import (
    Column, Integer, String, Date, UniqueConstraint, CheckConstraint, Index
)
from sqlalchemy.orm import relationship
from .Base import Base

class Season(Base):
    __tablename__ = "seasons"          # plural para consistência

    id          = Column(Integer, primary_key=True)
    year        = Column(Integer, nullable=False)
    start_date  = Column(Date, nullable=False)
    description = Column(String(120))

    __table_args__ = (
        UniqueConstraint("year", name="uq_season_year"),
        CheckConstraint("year >= 1950", name="ck_season_year_min"),
        Index("ix_season_year", "year"),
    )

    races     = relationship("Race", back_populates="season",
                             cascade="all, delete-orphan")
    contracts = relationship("DriverContract", back_populates="season",
                             cascade="all, delete-orphan")
