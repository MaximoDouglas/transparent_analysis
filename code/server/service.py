from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from facade.facade import Facade as fc
from model.dataConsumer import DataConsumer as dc

dc.getData(27, 2017, 2017)
