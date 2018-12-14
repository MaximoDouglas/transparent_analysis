from flask import request
from flask_restful import Resource

class Facade(Resource):
    def get(self,state,beginYear,endYear):
