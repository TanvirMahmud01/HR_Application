from datetime import date, datetime
from flask import Flask, render_template, url_for, request, redirect

from dbConnection import DB
import models
import dbConnection


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


current_date = date.today()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':

        result = request.form  # tuple containing key/value pair for email, phone & salary
        id = result["id"]
        email = result["email"]
        phone = result["phone"]
        salary = int(result["salary"])

        db = dbConnection.DB()
        db.update_employee(id, email, phone, salary)

        # sqlCmd = f'select {email}, first_name, last_name from hr_employees'

        return redirect('/home')
    else:
        employees = models.get_employees()
        return render_template('home.html', employees=employees)


@app.route('/newemployee',  methods=['GET', 'POST'])
def about():

    if request.method == 'POST':

        result = request.form  # tuple containing key/value pair for email, phone & salary
        first_name = result["first_name"]
        last_name = result["last_name"]
        email = result["email"]
        phone_number = result["phone_number"]
        hire_date = datetime.strptime(result["hire_date"], '%Y-%m-%d').date()
        job_id = result["job_id"]
        salary = int(result["salary"])
        manager_id = int(result["manager_id"])
        department_id = int(result["department_id"])

        db = dbConnection.DB()
        db.add_employee(first_name, last_name, email, phone_number,
                        hire_date, job_id, salary, manager_id, department_id)

        print(first_name, last_name, email, phone_number,
              hire_date, job_id, salary, manager_id, department_id)

        return redirect('/home')
    else:

        db = dbConnection.DB()
        jobs = db.fetch_jobs()
        managers = db.fetch_managers()
        departments = db.fetch_departments()
        return render_template('newemployee.html', title='New Employee', date=current_date, jobs=jobs, managers=managers, departments=departments)


if __name__ == '__main__':
    app.run(debug=True)
