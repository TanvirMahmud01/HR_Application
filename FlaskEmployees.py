from flask import Flask, render_template, url_for, request, redirect

from dbConnection import DB
import models


app = Flask(__name__)
# DB = dbConnection.db()
employees = models.get_employees()


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form
        # db = DB()
        # db.update_employee(100, 'sking')
        return redirect('home')
    else:
        return render_template('home.html', employees=employees)


@app.route('/about',  methods=['GET', 'POST'])
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
