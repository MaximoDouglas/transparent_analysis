import requests
import json
import csv
import pandas as pd

class DataConsumer():
    def getData(state, beginYear, endYear):
        labels = ['data','municipio','valorBF','qtdBeneficiadosBF']

        cities = DataConsumer.__getCities(state)
        data = DataConsumer.__getData(cities,state,beginYear,endYear);
        filePath = DataConsumer.__saveInFile(labels,data,state,beginYear,endYear)
        DataConsumer.__viewData(state,beginYear,endYear)

    def __saveInFile(labels,data,state,beginYear,endYear):
        file = open('./data/'+str(state)+str(beginYear)+str(endYear)+'.csv', 'w')
        csvwriter = csv.writer(file)

        csvwriter.writerow(labels)

        for row in data:
            csvwriter.writerow(row)

        file.close()

    def __getCities(state):
        cities = []

        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
        +str(state)+'/municipios').json()

        for city in response:
            cities.append(city['id'])

        return cities

    def __viewData(state,beginYear,endYear):
        df = pd.read_csv('./data/'+str(state)+str(beginYear)+str(endYear)+'.csv')
        print(df)

    def __getData(cities,state,beginYear,endYear):

        matrix = []

        for city in cities[:2]:
            cityInfo = []
            year = beginYear

            while(year <= endYear):
                for i in range(1, 3):
                    if i <= 9:
                        month = '0' + str(i)
                    else:
                        month = str(i)

                    cityInfo.append(requests.get('http://www.transparencia.gov.br/api-de-dados/'
                    +'bolsa-familia-por-municipio?mesAno='+str(year)+month+'&codigoIbge='+str(city)+'&pagina=1').json()[0])

                year += 1

            cleanInfo = DataConsumer.__preprocess(cityInfo)

            for info in cleanInfo:
                matrix.append(info)

        return matrix

    def __preprocess(rows):
        valSum = 0
        qtdSum = 0
        lines = []

        for row in rows:
            line = []
            labels = ['dataReferencia','municipio','valor','quantidadeBeneficiados']

            for label in labels:
                if (label == 'dataReferencia'):
                    line.append(str(row[label]).split("/")[1])
                elif (label == 'municipio'):
                    line.append(str(row[label]['nomeIBGE']))
                elif (label == 'valor'):
                    valSum += row[label]
                    line.append(str(row[label]))
                elif (label == 'quantidadeBeneficiados'):
                    qtdSum += row[label]
                    line.append(str(row[label]))
                else:
                    line.append(str(row[label]))

            lines.append(line)

        bnfMean = qtdSum/(len(lines))
        valMean = valSum/(len(lines))

        for line in lines:
            if (float(line[2]) >= valMean):
                line[2] = 'valorBF >= media'
            else:
                line[2] = 'valorBF < media'
            if (float(line[3]) >= bnfMean):
                line[3] = 'qtdBeneficiadosBF >= media'
            else:
                line[3] = 'qtdBeneficiadosBF < media'

        return lines
