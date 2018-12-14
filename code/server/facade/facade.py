from flask import request
from flask_restful import Resource
from model.dataConsumer import DataConsumer
from model.dataAnalyzer import DataAnalyzer

class Facade(Resource):
    def get(self,state,beginYear,endYear):
        filePath = DataConsumer.getData(state,beginYear,endYear)
        result = DataAnalyzer.analyze(filePath)

        print(result)

        #return result

class FacadeAux(Resource):
    def get(self):
        return 0
