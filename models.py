from typing import Optional
from pydantic import BaseModel, Field, StrictFloat
import dbConnection
import datetime


class employee_model(BaseModel):
    employee_id: int
    first_name: Optional[str]
    last_name: str
    email: str
    phone: Optional[str]
    hire_date: datetime.date
    job_id: str
    salary: Optional[int]
    commission: Optional[float]
    manager_id: Optional[int]
    department_id: Optional[int]


def build_class_list(tup):
    employees = []  # list of classes
    for row in tup:
        c = employee_model(
            employee_id=row[0],
            first_name=row[1].strip(),
            last_name=row[2],
            email=row[3],
            phone=row[4].strip(),
            hire_date=row[5],
            job_id=row[6],
            salary=row[7],
            commission=row[8],
            manager_id=row[9],
            department_id=row[10]
        )
        employees.append(c)
    return employees


def get_employees():
    db = dbConnection.DB()
    data = db.fetch_employee()
    return build_class_list(data)


if __name__ == "__main__":
    # for site in get_employees():
    #     print(f"{site.warehouse_name} ==> {site.location_id}\n")

    print(get_employees())

# column = ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME',
#  'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']
