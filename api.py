import requests
from flask import Flask, jsonify, request, abort, json
import requests

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return "Welcome"


##############api1############################

@app.route('/leagues', methods = ['GET'])
def get_legues():
    response = requests.get('https://www.thesportsdb.com/api/v1/json/1/all_leagues.php')
    if response.status_code == 200:
        print("Successful request!")
    else:
        print("Unsuccessful request!")
    return response.json()

@app.route('/leagues_by_id', methods = ['GET'])
def get_legues_by_id():

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    try:
        response = requests.get('https://www.thesportsdb.com/api/v1/json/1/lookupleague.php', params={'id': id}, timeout = 0.60)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        return response.json()

##########api2###################3

@app.route('/todo', methods = ['GET'])
def todo():

    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    return response.json()

@app.route('/todo_id', methods = ['GET'])
def get_todo_by_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."
    response = requests.get('https://jsonplaceholder.typicode.com/todos', params={'id': id})
    print("status : ", response.status_code)

    return response.text


#############api3##########################

@app.route('/httpbin/add', methods = ['POST'])
def add():
    data = {'title': 'Python Requests', 'body': 'Requests are awesome', 'userId': 10}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.post('https://httpbin.org/post', data_json, headers=headers, timeout = 0.60)
    except requests.Timeout as error:
        print("errr: ", error)
        return error
    else:
        return response.json()

@app.route('/httpbin/update', methods = ['PUT'])
def update():
    data = {'title': 'Python Requests', 'body': 'updated body', 'userId': 10}
    data_json = json.dumps(data)
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.put('https://httpbin.org/put', data_json, headers=headers)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)
    else:
        return response.json()


@app.route('/httpbin/delete', methods = ['DELETE'])
def delete():
    data = {'userId': 10}
    response = requests.delete('https://httpbin.org/delete',params = data)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)

