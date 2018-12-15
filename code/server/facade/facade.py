from flask import request
from flask_restful import Resource
import os
import datetime

from model.getData import GetData
from model.messageSaver import MessageSaver

class Facade(Resource):
    def get(self,state,beginYear,endYear):
        data = GetData.getData(state,beginYear,endYear)

        jsonList = []

        for value in data[2]:
            jsonList.append({'date': value[0], 'value': value[1]})

        return {'id': data[0], 'state_name': data[1], 'list': jsonList}

    def delete(self,id):
        filePath = './data/'+str(id)+'.csv'

        if (os.path.isfile(filePath)):
            os.remove(filePath)

    def put(self):
        requestBody = request.get_json()
        id = str(requestBody['id'])

        filePath = './data/'+str(id)+'.csv'

        if (os.path.isfile(filePath)):
            newName = requestBody['new_name']
            if(id[:2] != newName[:2]):
                os.rename(filePath, './data/'+id[:2]+'_'+newName+'.csv')

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
            files.remove('.gitignore')
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

    def __parameter_get(self, id):
        for hero in heroes:
            if hero['id'] == id:
                return hero
        return 'bad request!', 400

    def __simple_get(self):
        return heroes
