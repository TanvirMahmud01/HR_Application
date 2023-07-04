import cx_Oracle

conStr = 'COMP214_m23_er_22/password@199.212.26.208:1521/sqld'
conn = None


class DB():
    def __init__(self) -> None:
        pass

    def fetch_employee(self):
        conn = cx_Oracle.connect(conStr)

        sqlCmd = 'select * from hr_employees'
        try:
            cur = conn.cursor()
            print("Connected to DB!!!")

            cur.execute(sqlCmd)
            result = cur.fetchall()
            # df = pd.DataFrame.from_records(
            #     result, columns=[x[0] for x in cur.description])
            # columns = [x[0] for x in cur.description]

            cur.close()
            return result

        except Exception as err:
            print(f"Database error: {err}")

        finally:
            conn.close()

    def update_employee(self, id, email: str, phone: str, salary: int):
        sqlCmd = f"update hr_employees set email = :email, phone_number= :phone, salary= :salary where employee_id = :id"

        try:
            # establish a new connection
            'COMP214_m23_er_22/password@199.212.26.208:1521/sqld'
            with cx_Oracle.connect(user='COMP214_m23_er_22',
                                   password='password',
                                   dsn='199.212.26.208/sqld',
                                   encoding='UTF-8') as connection:
                # create a cursor
                with connection.cursor() as cursor:
                    # execute the insert statement
                    cursor.execute(sqlCmd, [email, phone, salary, id])
                    # commit the change
                    connection.commit()
        except cx_Oracle.Error as error:
            print(error)


if __name__ == '__main__':
    db = DB()
    db.update_employee(100, 'Tonmoy', '515.123.4567', 30000)
# column = ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER', 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID']
