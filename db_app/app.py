from flask import Flask, url_for, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///class_db.sqlite"

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)

    def __repr__(self):
        return '<Pet %r>' % (self.name)

class Class(db.Model):
    __tablename__ = "Class"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(225))
    hobby = db.Column(db.String(225))
    age = db.Column(db.Integer)

@app.route("/")
def index():
    results = db.session.query(Class.name, Class.hobby, Class.age)
    return render_template("index.html", results = results)

@app.route("/update", methods = ["POST"])
def update_db():
    name = request.form["name"]
    hobby = request.form["hobby"]
    age = request.form["age"]

    person = Class(name = name, hobby = hobby, age = age)
    db.session.add(person)
    db.session.commit()

    return redirect("/", code = 302)




if __name__ == "__main__":
    app.run(debug = True)
