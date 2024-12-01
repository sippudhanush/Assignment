from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud
import models
import database

app = FastAPI()


@app.post("/create-employee")
def create_employee(
    name: str, age: str, place: str, gender: str, db: Session = Depends(database.get_db)
):
    return crud.CreateEmployee(db=db, name=name, age=age, place=place, gender=gender)


@app.get("/get-all-employees")
def get_all_employees(db: Session = Depends(database.get_db)):
    return crud.get_all_employees(db=db)


@app.get("/get-employee-by-name/{emp_name}")
def get_employee_by_id(emp_name: str, db: Session = Depends(database.get_db)):
    db_employee = crud.get_employee_by_name(db=db, name=emp_name)
    return db_employee


@app.put("/update-employee")
def update_employee(
    name: str, age: str, place: str, gender: str, db: Session = Depends(database.get_db)
):
    db_employee = crud.update_employee(
        db=db, name=name, age=age, place=place, gender=gender
    )
    return db_employee


@app.delete("/delete-employee/{emp_name}")
def delete_employee(emp_name: str, db: Session = Depends(database.get_db)):
    db_employee = crud.delete_employee_by_name(db=db, name=emp_name)
    return db_employee
