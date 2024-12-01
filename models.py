from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, DateTime
from database import Base


class Employee(Base):
    __tablename__ = "employee"
    EmployeeName = Column(String, primary_key=True)
    EmployeeAge = Column(Integer, primary_key=True)
    EmployeePlace = Column(String, nullable=True)
    EmployeeGender = Column(String, nullable=True)
