from sqlalchemy.orm import Session
import models


def CreateEmployee(db: Session, name: str, age: str, place: str, gender: str):
    db_employee = models.Employee(
        EmployeeName=name, EmployeeAge=age, EmployeePlace=place, EmployeeGender=gender
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_all_employees(db: Session):
    return db.query(models.Employee).all()


def get_employee_by_name(db: Session, name: str):
    return (
        db.query(models.Employee).filter(models.Employee.EmployeeName == name).first()
    )


def update_employee(db: Session, name: str, age: str, place: str, gender: str):
    db_employee = (
        db.query(models.Employee).filter(models.Employee.EmployeeName == name).first()
    )
    if db_employee:
        db_employee.EmployeeName = name
        db_employee.EmployeeAge = age
        db_employee.EmployeePlace = place
        db_employee.EmployeeGender = gender
        db.commit()
        db.refresh(db_employee)
        return db_employee
    return None


def delete_employee_by_name(db: Session, name: str):
    db_employee = (
        db.query(models.Employee).filter(models.Employee.EmployeeName == name).first()
    )
    if db_employee:
        db.delete(db_employee)
        db.commit()
        return db_employee
    return None
