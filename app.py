import csv

from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


@app.route('/awards')
def awards():
    return render_template("awards.html")


@app.route("/registration")
def registration():
    return render_template("registration.html")


@app.route('/activities')
def activities():
    return render_template("activities.html")


@app.route('/keynotes')
def keynotes():
    return render_template("keynote.html")


@app.route('/meals')
def meals():
    return render_template("meals.html")


@app.route('/workshop')
def workshop():
    return render_template("workshopschedule.html")


@app.route('/poll')
def poll():
    return render_template("poll.html")


@app.route('/thankyou')
def thankyou():
    return render_template("thankyou.html")


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/nametags8')
def nametags8():
    return render_template("nametags8gen.html")


@app.route('/nametags10')
def nametags10():
    return render_template("nametags10gen.html")


if __name__ == '__main__':
    app.run()

with open('database_code/registrant_data_simplified.csv', mode='r') as csv_file:
    csvFile = csv.DictReader(csv_file)
    print(csvFile)
