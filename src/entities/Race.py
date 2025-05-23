from sqlalchemy import (
    Column, Integer, String, Date, ForeignKey,
    CheckConstraint, Index
)
from sqlalchemy.orm import relationship
from .Base import Base

class Race(Base):
    __tablename__ = "races"

    id         = Column(Integer, primary_key=True)
    name       = Column(String(120), nullable=False)
    race_date  = Column(Date, nullable=False)
    laps       = Column(Integer)
    weather    = Column(String(10))    

    season_id  = Column(Integer, ForeignKey("seasons.id"), nullable=False)
    circuit_id = Column(Integer, ForeignKey("circuits.id"), nullable=False)

    __table_args__ = (
        CheckConstraint("laps IS NULL OR laps > 0", name="ck_race_laps_positive"),
        CheckConstraint("weather IS NULL OR weather IN ('Dry','Wet','Mixed')",
                        name="ck_race_weather_enum"),
        Index("ix_race_season_date", "season_id", "race_date"),
    )

    season  = relationship("Season",  back_populates="races")
    circuit = relationship("Circuit", back_populates="races")
    results = relationship("Result",  back_populates="race",
                           cascade="all, delete-orphan")
