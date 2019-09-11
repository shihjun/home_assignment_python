from flask import Flask, jsonify, request
from extensions import db
from flask_migrate import Migrate
from models import Home
from schemas import HomeSchema
import csv


# "postgres://username:password@server:port/db_name"
url = "postgres://postgres:postgres@localhost:5432/homes_db"

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/seed")
def seed():
    with open("homes.csv", mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            x = Home()
            x.sell = row["Sell"]
            x.list = row[' "List"']
            x.living = row[' "Living"']
            x.rooms = row[' "Rooms"']
            x.beds = row[' "Beds"']
            x.baths = row[' "Baths"']
            x.age = row[' "Age"']
            x.acres = row[' "Acres"']
            x.taxes = row[' "Taxes"']

            db.session.add(x)
            db.session.commit()

        homes = Home.query.all()
        json_homes = HomeSchema(many=True).dump(homes)
        return jsonify(json_homes)


@app.route("/homes")
def get_book():
    sell = request.args.get("sell")
    list = request.args.get("list")
    living = request.args.get("living")
    rooms = request.args.get("rooms")
    beds = request.args.get("beds")
    baths = request.args.get("baths")
    age = request.args.get("age")
    acres = request.args.get("acres")
    taxes = request.args.get("taxes")
    query=Home.query
    if sell is not None:
        query = query.filter(Home.sell >= sell)
    if list is not None:
        query = query.filter(Home.list >= list)
    if living is not None:
        query = query.filter(Home.living >= living)
    if rooms is not None:
        query = query.filter(Home.rooms >= rooms)
    if beds is not None:
        query = query.filter(Home.beds >= beds)
    if baths is not None:
        query = query.filter(Home.baths >= baths)
    if age is not None:
        query = query.filter(Home.age >= age)
    if acres is not None:
        query = query.filter(Home.acres >= acres)
    if taxes is not None:
        query = query.filter(Home.taxes >= taxes)

    json_homes = HomeSchema(many=True).dump(query)
    return jsonify(json_homes)


app.run(debug=True)
