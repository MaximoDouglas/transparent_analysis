# Transparent Analysis
This repository contain both the client and the server of a client-server system that consumes and work on government data, especifically the Bolsa Família data.

## Installing and runing system

### Installing Service
1. Go to `~/transparent_analysis/code/service`.
2. If you already have **python3-pip, Flask, Flask-RESTful or flask-cors**, edit the file `start.sh` to comment the installation line of the dependence that you already have.
3. Run the command `bash start.sh`

If averything goes well, you have the service running on `http://localhost:4200/`.

