from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest
import os
import datetime

from model.getData import GetData
from model.messageSaver import MessageSaver

class Facade(Resource):
    def get(self,state,beginYear,endYear):
        data = GetData.getData(state,beginYear,endYear)

        jsonList = []
        if (type(data) == 'NoneType'):
            for value in data[2]:
                jsonList.append({'date': value[0], 'value': value[1]})

            return {'id': data[0], 'state_name': data[1], 'list': jsonList}
        else:
            raise BadRequest()

    def post(self):
        requestBody = request.get_json()

        name = requestBody['name']
        data = requestBody['content']
        date = datetime.datetime.now()

        MessageSaver.save(name,date,data)

        return {'name': name, 'content': data}

class FacadeCache(Resource):
    def get(self, id=None):
        if (len(request.args) == 0):
            if id is None:
                return self.__simple_get()
            else:
                return self.__parameter_get(id)
        else:
            param = request.args['name']
            l = []

            files = os.listdir('./data')
            names = []

            for file in files:
                names.append(file.split(".")[0])

            for id in names:
                if param.upper() in id.upper():
                    data = GetData.getById(id)

                    jsonList = []

                    for value in data[2]:
                        jsonList.append({'date': value[0], 'value': value[1]})

                    l.append({'id': data[0], 'state_name': data[1], 'list': jsonList})

            return l

    def put(self):
        requestBody = request.get_json()
        id = str(requestBody['id']).split("#")[0]

        filePath = './data/'+str(id)+'.csv'

        if (os.path.isfile(filePath)):
            newName = str(requestBody['id']).split("#")[1]
            if(id[:2] != newName[:2]):
                os.rename(filePath, './data/'+id[:2]+'_'+newName+'.csv')
            else:
                os.rename(filePath, './data/'+newName+'.csv')

    def delete(self,id):
        filePath = './data/'+str(id)+'.csv'

        if (os.path.isfile(filePath)):
            os.remove(filePath)

    def __parameter_get(self, id):
        files = os.listdir('./data')
        names = []

        for file in files:
            names.append(file.split(".")[0])

        for name in names:
            if (name.upper() == id.upper()):
                data = GetData.getById(id)

                jsonList = []

                for value in data[2]:
                    jsonList.append({'date': value[0], 'value': value[1]})

                return {'id': data[0], 'state_name': data[1], 'list': jsonList}

        return 'bad request!', 400

    def __simple_get(self):
        l = []

        files = os.listdir('./data')
        names = []

        for file in files:
            names.append(file.split(".")[0])

        for id in names:
            data = GetData.getById(id)

            jsonList = []

            for value in data[2]:
                jsonList.append({'date': value[0], 'value': value[1]})

            l.append({'id': data[0], 'state_name': data[1], 'list': jsonList})

        return l
