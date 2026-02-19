from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="tree_health_db"
)

cursor = db.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["POST"])
def add_data():
    tree = request.form["tree_name"]
    moisture = request.form["moisture"]
    temp = request.form["temperature"]
    humidity = request.form["humidity"]
    nutrients = request.form["nutrients"]

    sql = """INSERT INTO tree_data
             (tree_name, moisture, temperature, humidity, nutrients)
             VALUES (%s, %s, %s, %s, %s)"""
    values = (tree, moisture, temp, humidity, nutrients)

    cursor.execute(sql, values)
    db.commit()

    return redirect("/")

app.run(debug=True)
