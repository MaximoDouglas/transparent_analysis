from model.dataConsumer import DataConsumer as dc

class Facade():
    def get(state,beginYear,endYear):
        dc.getData(state, beginYear, endYear)
