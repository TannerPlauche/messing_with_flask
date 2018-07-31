from flask import Flask, request, jsonify
from flask import json

app = Flask(__name__)
app.config['TESTING'] = True

people = []


@app.route("/")
def hello():
    return "Hello world!"


@app.route("/name/<string:name>", methods=["GET", "POST"])
def sayHello(name):
    return "Hello there %s" % name


@app.route("/add/<string:name>", methods=["GET", "POST"])
def addPerson(name):
    people.append(name)
    return jsonify(people=people)


@app.route("/remove/<string:name>", methods=["GET", "POST"])
def removePerson(name):
    people.remove(name)
    return jsonify(people=people)


@app.route("/getpeople", methods=["GET", "POST"])
def getPeople():
    return jsonify(people=people)
