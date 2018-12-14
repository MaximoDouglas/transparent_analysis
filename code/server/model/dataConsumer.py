import requests
import json
import csv
import os
import pandas as pd

class DataConsumer():
    def getData(state, beginYear, endYear):
        labels = ['data','municipio','valorBF','qtdBeneficiadosBF']
        filePath = './data/'+str(state)+str(beginYear)+str(endYear)+'.csv'

        '''if (not os.path.isfile(filePath)):
            cities = DataConsumer.__getCities(state)
            data = DataConsumer.__getData(cities,state,beginYear,endYear);
            filePath = DataConsumer.__saveInFile(labels,data,state,beginYear,endYear)'''

        cities = DataConsumer.__getCities(state)
        data = DataConsumer.__getData(cities,state,beginYear,endYear);

        return filePath

    def __getCities(state):
        cities = []

        response = requests.get('https://servicodados.ibge.gov.br/api/v1/localidades/estados/'
        +str(state)+'/municipios').json()

        for city in response:
            cities.append(city['id'])

        return cities

    def __getData(cities,state,beginYear,endYear):

        matrix = []

        for city in cities[:2]:
            bf_Info = []
            gs_Info = []
            sd_Info = []
            year = beginYear

            while(year <= endYear):
                for i in range(1, 2):
                    if i <= 9:
                        month = '0' + str(i)
                    else:
                        month = str(i)

                    resultBF = requests.get('http://www.transparencia.gov.br/api-de-dados/'
                    +'bolsa-familia-por-municipio?mesAno='+str(year)+month+'&codigoIbge='+str(city)+'&pagina=1').json()[0]

                    resultGS = requests.get('http://www.transparencia.gov.br/api-de-dados/'
                    +'safra-por-municipio?mesAno='+str(year)+month+'&codigoIbge='+str(city)+'&pagina=1').json()[0]

                    resultSD = requests.get('http://www.transparencia.gov.br/api-de-dados/'
                    +'seguro-defeso-por-municipio?mesAno='+str(year)+month+'&codigoIbge='+str(city)+'&pagina=1').json()[0]

                    bf_Info.append(resultBF)
                    gs_Info.append(resultGS)
                    sd_Info.append(resultSD)

                year += 1

            cleanInfo = DataConsumer.__preprocess(bf_Info, gs_Info, sd_Info)

            for info in cleanInfo:
                matrix.append(info)

        return matrix

    def __preprocess(bf_Info, gs_Info, sd_Info):
        valSum = 0
        qtdSum = 0
        lines = []

        for i in range(len(bf_Info)):
            line = []
            labels = ['dataReferencia','municipio','valor','quantidadeBeneficiados']

            for label in labels:
                if (label == 'dataReferencia'):
                    month = 'month: '+str(str(bf_Info[i][label]).split("/")[1])
                    line.append(month)
                elif (label == 'municipio'):
                    line.append(str(bf_Info[i][label]['nomeIBGE']))
                elif (label == 'valor'):
                    valSum += bf_Info[i][label]
                    line.append(str(bf_Info[i][label]))
                elif (label == 'quantidadeBeneficiados'):
                    qtdSum += bf_Info[i][label]
                    line.append(str(bf_Info[i][label]))
                else:
                    line.append(str(bf_Info[i][label]))

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
