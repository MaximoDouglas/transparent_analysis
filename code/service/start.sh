#Export the application to the server
export FLASK_APP=service.py;

#Defines that the actual environment are in production (this will deactivate the debugger mode)
export FLASK_ENV=development;

#Runs the server
flask run;
