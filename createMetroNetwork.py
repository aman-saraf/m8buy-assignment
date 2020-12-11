from bson.objectid import ObjectId
from flask import (Flask, request)
from metro_models import Metro, Line, Station
import json
from pymodm.errors import ValidationError


def handler(event, context):
    request = json.loads(event['body'])
    metroName = request['name']
    lines = request['lines']
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
        return {"statusCode": 500, "body": json.dumps({"success": False, "error": error})}
    return {"statusCode": 200, "body": json.dumps({"success": True})}
