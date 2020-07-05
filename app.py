from datetime import datetime

import mysql
from flask import Flask, render_template, request, json, Response
from flask_expects_json import expects_json

from models import plant
from models.plant import Plant
from sensor_stuff import sensor
from service.plant_service import insertToDatabase, get_plant_from_db
from util.Encoder import MyEncoder

app = Flask(__name__)

plant_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'opt_Humidity': {'type': 'number'},
    },
    'required': ['name', 'opt_Humidity']
}


@app.route('/humidity/<port>/<seconds>', methods=['GET'])
@app.route('/humidity/', defaults={'seconds': 4, 'port': 'COM4'})
def request_to_arduino(seconds, port):
    # todo send request via serial port and wait for it and then wait for it
    # data = sensor.processRequest(port, seconds)
    return render_template('main.html', seconds=seconds)


@app.route('/add/plant/', methods=['POST'])
@expects_json(plant_schema)
def add_plant():
    plant = insertToDatabase(Plant(request.get_json()))
    return Response(response=json.dumps(vars(plant)), status=201)


@app.route('/plant/<plant_id>', methods=['GET'])
@app.route('/plant/', defaults={'plant_id': None})
def get_plant(plant_id):
    plant = get_plant_from_db(plant_id)
    return Response(response=MyEncoder().encode(plant), status=200)


@app.errorhandler(mysql.connector.Error)
def handle_bad_request(e):
    error = {"status": 400, "message": "Database connection failed", "date": datetime.now()}
    return json.dumps(error)


# @app.errorhandler(Exception)
# def handle_bad_request(e):
#     error = {"status": 400, "message": "Something went wrong", "date": datetime.now()}
#     return json.dumps(error)


if __name__ == '__main__':
    app.run()
