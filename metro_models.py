from pymodm import MongoModel, EmbeddedMongoModel, fields,  connect

connect('mongodb+srv://aman:test123@sydney-metro.tuzel.mongodb.net/sydney-metro?retryWrites=true&w=majority')

class Metro(MongoModel):
    name = fields.CharField()
    lines = fields.EmbeddedDocumentListField('Line')


class Line(EmbeddedMongoModel):
    name = fields.CharField()
    stations = fields.EmbeddedDocumentListField('Station')


class Station(EmbeddedMongoModel):
    name = fields.CharField()    