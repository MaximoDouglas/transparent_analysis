# Transparent Analysis
This repository contain both the client and the server of a client-server system that consumes and work on government data, especifically the Bolsa Família data.

## Installing and running system
`Note: the installations have to occur in different terminals.`

### Installing Service
0. Open a terminal.
1. Go to `~/transparent_analysis/code/service`.
2. If you already have **python3-pip, Flask, Flask-RESTful or flask-cors**, edit the file `start.sh` to comment the installation line of the dependence that you already have.
3. Run the command `bash start.sh`.
4. If everything gone well, you have the service running on `http://localhost:5000/`.
5. After the step **3**, the service dependences are now installed and you can edit the file `start.sh` to comment all the lines that installs external dependences.
 
### Installing Client
0. Open a terminal.
1. Go to `~/transparent_analysis/code/client`.
2. If you already have **curl, nodejs or angularCLI**, edit the file `start.sh` to comment the installation line of the dependence that you already have.
3. Run the command `bash start.sh`.
4. If everything gone well, you have the client running on `http://localhost:4200/`.
4.1. Note: perhaps you see a ERROR message in the system log. If this occurs, don't worry, the application works without any problems.
5. After the step **3**, the client dependences are now installed and you can edit the file `start.sh` to comment all the lines that installs external dependences.
