from sqlalchemy import (
    Column, Integer, String, UniqueConstraint, CheckConstraint, Index
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from .Base import Base

class Team(Base):
    __tablename__ = "teams"

    id           = Column(Integer, primary_key=True)
    name         = Column(String(80), nullable=False)
    logo_url     = Column(String(250))
    base_country = Column(String(3))            
    principal    = Column(String(80))
    founded_year = Column(Integer)

    __table_args__ = (
        UniqueConstraint("name", name="uq_team_name"),
        CheckConstraint("char_length(base_country)=3", name="ck_team_country_len"),
        CheckConstraint("founded_year BETWEEN 1950 AND EXTRACT(YEAR FROM CURRENT_DATE)",
                        name="ck_team_year_range"),
        Index("ix_team_country", "base_country"),
    )

    contracts = relationship("DriverContract", back_populates="team",
                             cascade="all, delete-orphan")
    results   = relationship("Result", back_populates="team")
