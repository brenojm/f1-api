from sqlalchemy import (
    Column, Integer, ForeignKey, UniqueConstraint,
    CheckConstraint, Index, Float
)
from sqlalchemy.orm import relationship
from .Base import Base

class DriverContract(Base):
    __tablename__ = "driver_contracts"

    id        = Column(Integer, primary_key=True)
    season_id = Column(Integer, ForeignKey("seasons.id"),  nullable=False)
    team_id   = Column(Integer, ForeignKey("teams.id"),    nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"),  nullable=False)
    number    = Column(Integer, nullable=False)
    salary_musd = Column(Float)   

    __table_args__ = (
        UniqueConstraint("season_id", "number",  name="uq_season_number"),
        UniqueConstraint("season_id", "driver_id", name="uq_driver_one_team"),
        UniqueConstraint("season_id", "team_id", "driver_id", name="uq_ct_unique"),
        CheckConstraint("number BETWEEN 1 AND 99", name="ck_driver_number_range"),
        Index("ix_contract_season_team", "season_id", "team_id"),
    )

    season = relationship("Season", back_populates="contracts")
    team   = relationship("Team",   back_populates="contracts")
    driver = relationship("Driver", back_populates="contracts")
