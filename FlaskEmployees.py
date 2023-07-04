from flask import Flask, render_template, url_for, request, redirect

from dbConnection import DB
import models
import dbConnection


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


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
        updated = db.update_employee(id, email, phone, salary)

        # sqlCmd = f'select {email}, first_name, last_name from hr_employees'

        # db = DB()
        # db.update_employee(100, 'sking')
        return redirect('/home')
    else:
        employees = models.get_employees()
        return render_template('home.html', employees=employees)


@app.route('/about',  methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
