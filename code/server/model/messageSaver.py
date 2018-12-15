import os
import csv

class MessageSaver():
    def save(name,date,data):
        filePath = './contacts/'+str(name)+'.csv'

        if (os.path.isfile(filePath)):
            file = open(filePath, 'a')
            csvwriter = csv.writer(file)
        else:
            file = open(filePath, 'w')
            csvwriter = csv.writer(file)
            csvwriter.writerow(['date','content'])


        row = []

        row.append(date)
        row.append(data)

        csvwriter.writerow(row)

        file.close()

        return filePath
