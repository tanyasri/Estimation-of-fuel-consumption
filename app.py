import numpy as np
import pickle
from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

conn = mysql.connector.connect(host="localhost", user='root', password='', database='user')
cursor = conn.cursor()


@app.route('/')
def about():
    return render_template('welcome.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def about1():
    return render_template('register.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `LOGIN_DETAILS` WHERE `email` LIKE '{}' AND `password` LIKE '{}'""".format(email, password))
    users = cursor.fetchall()
    if len(users) > 0:
        return redirect('/index')
    else:
        return render_template('login.html' , info='Invalid User,try again!')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('uname')
    email = request.form.get('uemail')
    password = request.form.get('upassword')

    cursor.execute(
        """INSERT INTO `LOGIN_DETAILS`(`user_id`, `name`,`email`,`password`) VALUES (NULL,'{}','{}','{}')""".format(name, email,
                                                                                                            password))
    conn.commit()
    return render_template('index.html')


@app.route('/index/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template("result.html", pred='Prediction of the fuel consumption from the given data is {}'.format(
        output) + ' gallon/hour')


@app.route('/index', methods=['POST'])
def indexCalling():
    return render_template('index.html')


@app.route('/welcome')
def homeCalling():
    return render_template('welcome.html')


@app.route('/about')
def aboutCalling():
    return render_template('about.html')


@app.route('/generator')
def generatorCalling():
    return render_template('generator.html')


@app.route('/social')
def socialCalling():
    return render_template('social.html')


@app.route('/contact')
def contactCalling():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
