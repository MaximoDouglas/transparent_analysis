# Transparent Analysis
This repository contain both the client and the server of a client-server system that consumes and work on government data, especifically the Bolsa Família data.

## Running system
`Note: the installations have to occur in different terminals.`

### Installing Service
0. Required packeges: **python3-pip, Flask, Flask-RESTful and flask-cors**;
1. Open a terminal;
2. Go to `~/transparent_analysis/code/service`;
3. Run the command `bash start.sh`;
4. If everything gone well, you have the service running on `http://localhost:5000/`.
 
### Installing Client
0. Required packeges: **curl, nodejs and angularCLI**;
1. Open a terminal;
2. Go to `~/transparent_analysis/code/client`;
3. Run the command `bash start.sh`.
4. If everything gone well, you have the client running on `http://localhost:4200/`. Note: perhaps you see a ERROR message in the system log. If this occurs, don't worry, the application works without any problems.

## Using Client app
1. [This Link](https://www.youtube.com/watch?v=JXqDNV4YhwU) shows the general usage of the app. 
2. Na tela inicial, é possivel ver uma barra mais ao topo, com as descrições **Main** | **Data-List** | **Contact**, cada uma fornece serviçoes diferentes.
3. Na aba **Main** (na qual a aplicação abre inicialmente) dois itens: **Links em forma de botão** e **Uma caixa de texto**.
- 3.1. O usuário pode verificar os conteúdos dos 4 links externos, pois podem ser uteis para o uso do Sistema.
- 3.2. Na **Caixa de texto** o usuário pode digitar um ID para procurar dados que estejam no cache do servidor e tenham ID similar.
4. Na aba **Data-List** existem dois subcomponentes: **Form** e **Lista de dados do cache do servidor** (If there are data in the server cache).
- 4.1. In the **Form** the user can fill the code of a state a begin year and a end year to make the request pressing **SEND**. Doing this, the user will send a GET Request to the server. If the data for the respective request is already in the server, the server will just process and send the response. If the data is not in the server, the service will consume the IBGE and the Portal da transparência API to get and, after it, process the data requested by the user.
- 4.2. The **List of cache data** are, as the name says, a list of data that already are on the server cache. Cliking in one of these items will take you to the component **Data Detail**.
- 4.3. The **Data detail** component have a series of informations about the data, including a chart representing the sum of the Bolsa Familia values that the cities of the respective state had received in a interval of time. In this component there are a **Text Box** that will be explained as follows.
- 4.4. The **Text Box** in the **Data detail** component is used to make the PUT request, updating the data ID with the new one.
5. In the **Contact tab** the user can send a feedback message to the server, along with his name. The last message sent by the user will appear in the bottom of the page.

## Using the Service API
### GET Requests
1. To get the data in the interval of {beginYear} 'til the {endYear} from a state that have the id = {stateCode} use: `http://127.0.0.1:5000/{stateCode}/{beginYear}/{endYear}`
2. To get a list with the data in cache do servidor that have the ID similar to {id}, use: `http://127.0.0.1:5000/cache?name={id}`.
3. To get the cache do servidor data that ID matches **exactly** with {id}, use: `http://127.0.0.1:5000/cache/{id}`.
4. To get all the data in cache do servidor, use: `http://127.0.0.1:5000/cache`.

### PUT Request
1. To update the id of a data file that have the id = {id} with another id = {newId}, use: `http://127.0.0.1:5000/cache`, with the request body like: `{"id": "{id}#{newId}", "state_name": "Alagoas", "list": []}`.

### POST Request
1. To send a feedback message to the server, use: `http://127.0.0.1:5000/`, with the request body like: `{"name":"Douglas", "content": "Gostei muito desse sistema"}`

### DELETE Request
1. To delete the cache do servidor data that ID matches **exactly** with {id}, use: `http://127.0.0.1:5000/cache/{id}`.

