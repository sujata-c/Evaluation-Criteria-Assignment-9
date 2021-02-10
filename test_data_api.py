from flask import Flask, jsonify, request, abort
import requests

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route('/')
def index():
    return "Welcome"



@app.route('/books/all', methods = ['GET'])
def get():
    return jsonify(books)


@app.route('/books', methods = ['GET'])            # baseurl/books?id=2
def get_id():                                       # Data passed through URLs like this (after the ?) are called query parameters
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)


@app.route('/books', methods = ['POST'])
def create_book():
    if not request.json or not 'title' in request.json:
        abort(400)
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': 'Samuel R. Delany',
        'first_sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
    books.append(book)
    return jsonify({'created': book})


@app.route('/books/<int:id>', methods = ['PUT'])
def update(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    books[id]['title'] = "updated title"
    return jsonify({'update':books[id]})


@app.route('/books/del/<int:id>', methods=['DELETE'])
def delete_task(id):
    book = [book for book in books if book['id'] == id]
    if len(book) == 0:
        abort(404)
    books.remove(book[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
