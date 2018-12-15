#Install python3, comment if you already have it
#sudo apt-get install python3-pip;

#Install pip, comment if you already have it
#sudo apt-get install python3-pip;

#install data mining package
#pip3 install orange3

#Install Flask, comment if you already have it
#pip3 install Flask;

#Install Flask-RESTful, comment if you already have it
#pip3 install Flask-RESTful;

#Install flask_cors, comment if you already have it
#pip3 install -U flask-cors

#Export the application to the server
export FLASK_APP=service.py;

#Defines that the actual environment are in production (this will deactivate the debugger mode)
export FLASK_ENV=development;

#Runs the server
flask run;
