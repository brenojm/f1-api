from sqlalchemy import (
    Column, Integer, String, Date, CheckConstraint, Index
)
from sqlalchemy.orm import relationship
from .Base import Base

class Driver(Base):
    __tablename__ = "drivers"

    id            = Column(Integer, primary_key=True)
    full_name     = Column(String(120), nullable=False)
    nationality   = Column(String(3))         
    date_of_birth = Column(Date)
    image_url     = Column(String(250))

    __table_args__ = (
        CheckConstraint("char_length(nationality)=3", name="ck_driver_nat_len"),
        CheckConstraint("date_of_birth < CURRENT_DATE", name="ck_driver_dob_past"),
        Index("ix_driver_nat", "nationality"),
    )

    contracts = relationship("DriverContract", back_populates="driver",
                             cascade="all, delete-orphan")
    results   = relationship("Result", back_populates="driver")
