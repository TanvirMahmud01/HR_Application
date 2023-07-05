import oracledb
import config

connection = oracledb.connect(
    user=config.username, password=config.password, dsn=config.dsn)


class DB():
    def __init__(self) -> None:
        pass

    def fetch_employee(self):
        conn = oracledb.connect(user=config.username,
                                password=config.password, dsn=config.dsn)

        sqlCmd = 'select * from hr_employees order by employee_id desc'
        try:
            cur = conn.cursor()
            print("Connected to DB!!!")

            cur.execute(sqlCmd)
            result = cur.fetchall()

            cur.close()
            return result

        except Exception as err:
            print(f"Database error: {err}")

        finally:
            conn.close()

    def update_employee(self, id, email: str, phone, salary):
        sqlCmd = "update hr_employees set email = :email, phone_number= :phone, salary= :salary where employee_id = :id"

        try:
            with oracledb.connect(user=config.username,
                                  password=config.password, dsn=config.dsn,
                                  encoding='UTF-8') as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sqlCmd, [email, phone, salary, id])
                    # commit the change
                    connection.commit()
        except oracledb.Error as error:
            print(error)

    def add_employee(self, first_name: str, last_name: str, email, phone_number, hire_date, job_id,  salary, manager_id, department_id):

        try:
            with oracledb.connect(user=config.username,
                                  password=config.password, dsn=config.dsn,
                                  encoding='UTF-8') as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # calling procedure to insert employee
                    cursor.callproc('employee_hire_sp', [first_name, last_name, email, phone_number,
                                                         hire_date, job_id, salary, manager_id, department_id])

        except oracledb.Error as error:
            print(error)

    def fetch_jobs(self):
        sqlCmd = "select * from hr_jobs"
        try:

            with oracledb.connect(user=config.username,
                                  password=config.password, dsn=config.dsn,
                                  encoding='UTF-8') as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    cursor.execute(sqlCmd)
                    result = cursor.fetchall()
                    return result

        except oracledb.Error as error:
            print(error)

    def fetch_managers(self):
        sqlCmd = '''
                        SELECT 
                            sup.employee_id as manager_id,
                            sup.first_name,
                            sup.last_name
                        FROM hr_employees sub
                        JOIN hr_employees sup
                        ON sub.manager_id = sup.employee_id
                        GROUP BY sup.employee_id, sup.first_name, sup.last_name
                        order by sup.employee_id
                 '''
        try:

            with oracledb.connect(user=config.username,
                                  password=config.password, dsn=config.dsn,
                                  encoding='UTF-8') as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    cursor.execute(sqlCmd)
                    result = cursor.fetchall()
                    return result

        except oracledb.Error as error:
            print(error)

    def fetch_departments(self):
        sqlCmd = '''
                        select department_id, department_name from hr_departments
                 '''
        try:

            with oracledb.connect(user=config.username,
                                  password=config.password, dsn=config.dsn,
                                  encoding='UTF-8') as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    cursor.execute(sqlCmd)
                    result = cursor.fetchall()
                    return result

        except oracledb.Error as error:
            print(error)


if __name__ == '__main__':
    db = DB()
    r = db.fetch_employee()
    print(r)
    pass
