# Transparent Analysis
This repository contain both the client and the server of a client-server system that consumes and work on government data, especifically the Bolsa Família data.

## Running system
`Note: the installations have to occur in different terminals.`

### Installing Service
0. Required packeges: **python3-pip, Flask, Flask-RESTful or flask-cors**;
1. Open a terminal;
2. Go to `~/transparent_analysis/code/service`;
3. Run the command `bash start.sh`;
4. If everything gone well, you have the service running on `http://localhost:5000/`.
 
### Installing Client
0. Required packeges: **curl, nodejs or angularCLI**;
1. Open a terminal;
2. Go to `~/transparent_analysis/code/client`;
3. Run the command `bash start.sh`.
4. If everything gone well, you have the client running on `http://localhost:4200/`. Note: perhaps you see a ERROR message in the system log. If this occurs, don't worry, the application works without any problems.

## Using the Service API
### GET Requests
1. To get the data in the interval of {beginYear} 'til the {endYear} from a state that have the id = {stateCode} use: `http://127.0.0.1:5000/{stateCode}/{beginYear}/{endYear}`
2. To get a list with the data in cache that have the ID similar to {id}, use: `http://127.0.0.1:5000/cache?name={id}`.
3. To get the cache data that ID matches **exactly** with {id}, use: `http://127.0.0.1:5000/cache/{id}`.
4. To get all the data in cache, use: `http://127.0.0.1:5000/cache`.

### PUT Request
1. To update the id of a data file that have the id = {id} with another id = {newId}, use: `http://127.0.0.1:5000/cache`, with the request body like: `{"id": "{id}#{newId}", "state_name": "Alagoas", "list": []}`.

### POST Request
1. To send a feedback message to the server, use: `http://127.0.0.1:5000/`, with the request body like: `{"name":"Douglas", "content": "Gostei muito desse sistema"}`

### DELETE Request
1. To delete the cache data that ID matches **exactly** with {id}, use: `http://127.0.0.1:5000/cache/{id}`.

