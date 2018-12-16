from flask_cors import CORS
from flask import Flask
from flask_restful import Api
from facade.facade import Facade
from facade.facade import FacadeCache

#Creates an app based on Flask
app = Flask(__name__)

cors = CORS(app)

#Creates an api manager that will route the requests
api = Api(app)

#Routing the requests to "/".
#In this case, the class HelloWorld will be the responsible to handle this requests
api.add_resource(Facade,'/', '/<int:state>/<int:beginYear>/<int:endYear>')
api.add_resource(FacadeCache, '/cache', '/cache/<string:id>','/cache/')

#This conditional allow the running just if this script is directly executed
if __name__ == '__main__':
	app.run(debug=True)
