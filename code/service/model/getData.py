import requests
import json
import csv
import os
import pandas as pd

class GetData():
    def getData(state, beginYear, endYear):
        labels = ['data','valorBF']
        filePath = './data/'+str(state)+str(beginYear)+str(endYear)+'.csv'

        id = str(state)+str(beginYear)+str(endYear)
        data = []

        if (not os.path.isfile(filePath)):

            cities = GetData.__getCities(state)
            data = GetData.__getData(cities,state,beginYear,endYear);
            filePath = GetData.__saveInFile(labels,data,state,beginYear,endYear)
        else:
            df = pd.read_csv(filePath)
            data = df.values.tolist()

        stateName = GetData.__getStateName(state)

        return (id, stateName, data)

    def getById(id):
        filePath = './data/'+str(id)+'.csv'

        df = pd.read_csv(filePath)
        data = df.values.tolist()

        stateName = GetData.__getStateName(str(id)[:2])

        return (id, stateName, data)

    def __getCities(state):
        cities = []

        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
        +str(state)+'/municipios').json()

        for city in response:
            cities.append(city['id'])

        return cities

    def __getStateName(id):
        
        states = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados').json()

        for state in states:
            if (str(state['id']) == str(id)):
                return state['nome']

    def __getData(cities,state,beginYear,endYear):
        matrix = []

        year = beginYear

        while(year <= endYear):
            for i in range(1, 3):
                bf_Info = []

                if i <= 9:
                    month = '0' + str(i)
                else:
                    month = str(i)

                for city in cities[:2]:
                    resultBF = requests.get('http://www.transparencia.gov.br/api-de-dados/'
                    +'bolsa-familia-por-municipio?mesAno='+str(year)+month+'&codigoIbge='+str(city)
                    +'&pagina=1').json()[0]

                    bf_Info.append(resultBF)

                cleanInfo = GetData.__preprocess(bf_Info)

                matrix.append(cleanInfo)

            year += 1

        return matrix

    def __preprocess(bf_Info):
        valSum = 0
        line = []

        dateStr = str(bf_Info[0]['dataReferencia'])
        date = dateStr.split("/")[1]+'-'+dateStr.split("/")[2]

        for i in range(len(bf_Info)):
            valSum += bf_Info[i]['valor']

        line.append(date)
        line.append(valSum)

        return line

    def __saveInFile(labels,data,state,beginYear,endYear):
        filePath = './data/'+str(state)+str(beginYear)+str(endYear)+'.csv'
        file = open(filePath, 'w')
        csvwriter = csv.writer(file)

        csvwriter.writerow(labels)

        for row in data:
            csvwriter.writerow(row)

        file.close()

        return filePath

    def __viewData(state,beginYear,endYear):
        df = pd.read_csv('./data/'+str(state)+str(beginYear)+str(endYear)+'.csv')
        print(df)
