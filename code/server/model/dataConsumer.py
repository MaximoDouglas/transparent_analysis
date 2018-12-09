import requests
import json
import csv
import pandas as pd

class DataConsumer():
    def getData(state, beginYear, endYear):

        cities = DataConsumer.__getCities(state)

        responses = []
        year = beginYear

        while(year <= endYear):
            for city in cities[:1]:
                for i in range(1, 13):
                    if i <= 9:
                        month = '0' + str(i)
                    else:
                        month = str(i)

                    request = requests.get('http://www.transparencia.gov.br/api-de-dados/'
                    +'bolsa-familia-por-municipio?mesAno='+str(year)+month+'&codigoIbge='+str(city)+'&pagina=1')

                    responses.append(request.json())

                year += 1

        DataConsumer.__viewData(responses, state, beginYear, endYear)

    def __getCities(state):
        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
        +str(state)+'/municipios').json()

        cities = []

        for city in response:
            cities.append(city['id'])

        return cities

    def __viewData(responses, state, beginYear, endYear):
        bdata = open('./data/'+str(state)+str(beginYear)+str(endYear)+'.csv', 'w')
        csvwriter = csv.writer(bdata)

        line = 0

        for response in responses:
            rows = []
            for js in response:
                if line == 0:
                    header = ['data','municipio','valor','quantidadeBeneficiados']
                    csvwriter.writerow(header)
                    line += 1

                features = ['dataReferencia','municipio','valor','quantidadeBeneficiados']

                val = []
                for feature in features:
                    if (feature == 'municipio'):
                        val.append(str(js[feature]['nomeIBGE']))
                    elif (feature == 'quantidadeBeneficiados'):
                        val.append(str(js[feature]))
                    else:
                        val.append(str(js[feature]))

                csvwriter.writerow(val)

        bdata.close()

        df = pd.read_csv('./data/'+str(state)+str(beginYear)+str(endYear)+'.csv')

        print(df)
