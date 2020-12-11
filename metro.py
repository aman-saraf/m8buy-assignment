from bson.objectid import ObjectId
from flask import (Flask, request)
from metro_models import Metro, Line, Station
import json
from pymodm.errors import ValidationError
app = Flask(__name__)


@app.route('/metro', methods=['POST'])
def create_metro():
    metroName = request.json['name']
    lines = request.json['lines']
    metroStations = []
    metroLines = []
    for line in lines:
        for station in line['stations']:
            metroStations.append(Station(station['name']))
        metroLines.append(Line(line['name'], metroStations))
    metro = Metro(metroName, metroLines)
    try:
        metro.save()
    except ValidationError as error:
        return {"success": False, "error": error}
    return {"success": True}


if __name__ == '__main__':
    app.run(debug=True)
