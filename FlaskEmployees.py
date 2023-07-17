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
        salary = int(result["salary"]) if result["salary"] != '' else ''
        db = dbConnection.DB()
        db.update_employee(id, email, phone, salary)
        return redirect(url_for('home'))
    else:
        employees = models.get_employees()
        return render_template('home.html', employees=employees)


@app.route('/newemployee',  methods=['GET', 'POST'])
def newemployee():
    if request.method == 'POST':
        result = request.form
        first_name = result["first_name"]
        last_name = result["last_name"]
        email = result["email"]
        phone_number = result["phone_number"]
        hire_date = datetime.strptime(result["hire_date"], '%Y-%m-%d').date()
        job_id = result["job_id"]
        salary = int(result["salary"]) if result["salary"] != '' else ''
        manager_id = int(result["manager_id"]
                         ) if result["manager_id"] != '' else ''
        department_id = int(result["department_id"]
                            ) if result["department_id"] != '' else ''
        db = dbConnection.DB()
        db.add_employee(first_name, last_name, email, phone_number,
                        hire_date, job_id, salary, manager_id, department_id)
        return redirect(url_for('home'))
    else:
        db = dbConnection.DB()
        jobs = db.fetch_jobs()
        managers = db.fetch_managers()
        departments = db.fetch_departments()
        return render_template('newemployee.html', title='New Employee', date=current_date, jobs=jobs, managers=managers, departments=departments)


@app.route('/identifyjob', methods=['GET', 'POST'])
def identifyjob():
    db = dbConnection.DB()
    job_description = None
    if request.method == 'POST':
        job_id = request.form["job_id"]
        job_description = db.get_job_description(job_id)
    return render_template('identifyjob.html', job_description=job_description)


@app.route('/updatejob', methods=['GET', 'POST'])
def updatejob():
    db = dbConnection.DB()
    message = None

    if request.method == 'POST':
        job_id = request.form["job_id"]
        job_title = request.form["job_title"]
        min_salary = int(
            request.form["min_salary"]) if request.form["min_salary"] != '' else None
        max_salary = int(
            request.form["max_salary"]) if request.form["max_salary"] != '' else None

        try:
            db.update_job(job_id, job_title, min_salary, max_salary)
            message = "Job updated successfully"
        except Exception as e:
            message = str(e)

    jobs = db.fetch_jobs()
    return render_template('updatejob.html', jobs=jobs, message=message)


if __name__ == '__main__':
    app.run(debug=True)
