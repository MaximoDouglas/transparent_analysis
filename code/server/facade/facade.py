from flask import request
from flask_restful import Resource

from model.dataConsumer import DataConsumer as dc

class Facade(Resource):
    def get(self,state,beginYear,endYear):
        return dc.getData(state,beginYear,endYear)
