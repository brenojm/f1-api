from sqlalchemy import (
    Column, Integer, Boolean, ForeignKey,
    UniqueConstraint, CheckConstraint, Index
)
from sqlalchemy.orm import relationship
from .Base import Base

class Result(Base):
    __tablename__ = "results"

    id        = Column(Integer, primary_key=True)
    race_id   = Column(Integer, ForeignKey("races.id"),   nullable=False)
    team_id   = Column(Integer, ForeignKey("teams.id"),   nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id", ondelete="RESTRICT"), nullable=False)

    position  = Column(Integer, nullable=False)
    points    = Column(Integer, nullable=False)
    fastest_lap = Column(Boolean, nullable=False, server_default="false")

    __table_args__ = (
        UniqueConstraint("race_id", "driver_id", name="uq_result_unique"),
        CheckConstraint("points BETWEEN 0 AND 25", name="ck_points_range"),
        CheckConstraint("position BETWEEN 1 AND 20", name="ck_position_range"),
        Index("ix_result_driver_race", "driver_id", "race_id"),
    )

    race   = relationship("Race",   back_populates="results")
    team   = relationship("Team",   back_populates="results")
    driver = relationship("Driver", back_populates="results")
