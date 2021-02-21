# Knowledge of working with REST APIs

**Problem definition**
---------------------------------------------------------------------------------------------------------------------------------------------

Understand REST APIs. Write sample program and include at least 3 different API invocations. Handle exceptions and timing issues.

- What is an API?

The term API, short for Application Programming Interface, refers to a part of a computer program designed to be used or manipulated by another program, as opposed to an interface designed to be used or manipulated by a human. Computer programs frequently need to communicate amongst themselves or with the underlying operating system, and APIs are one way they do it. 

- What is REST?

The characteristics of a REST system are defined by six design rules:

1. Client-Server: There should be a separation between the server that offers a service, and the client that consumes it.
2. Stateless: Each request from a client must contain all the information required by the server to carry out the request.
3.Cacheable: The server must indicate to the client if requests can be cached or not.
4.Layered System: Communication between a client and a server should be standardized in such a way that allows intermediaries to respond to requests instead of the end server, without the client having to do anything different.
5. Uniform Interface: The method of communication between a client and a server must be uniform.
6. Code on demand: Servers can provide executable code or scripts for clients to execute in their context. This constraint is the only one that is optional.

- The Request: When you want to interact with data via a REST API, this is called a request.
A request is made up of the following components:

1. Endpoint – The URL that delineates what data you are interacting with. Similar to how a web page URL is tied to a specific page, an endpoint URL is tied to a specific resource within an API.

2. Method – Specifies how you’re interacting with the resource located at the provided endpoint. REST APIs can provide methods to enable full Create, Read, Update, and Delete (CRUD) functionality. Here are common methods most REST APIs provide:

        GET – Retrieve data
        PUT – Replace data
        POST – Create data
        DELETE – Delete data
3. Data – If you’re using a method that involves changing data in a REST API, you’ll need to include a data payload with the request that includes all data that will be created or modified.

4. Headers – Contain any metadata that needs to be included with the request, such as authentication tokens, the content type that should be returned, and any caching policies.

- The Response: When you perform a request, you’ll get a response from the API. Just like in the request, it’ll have a response header and response data, if applicable. 

**Installation**
--------------------------------------------------------------------
Requirements:

- Python 3.6+
- Flask 1.1.+

Install using pip:

        $ pip install flask
Import and initialize your application:

        from flask import Flask
        app = Flask(__name__)
        
**Example**

*How Request Data With GET*

            import requests
            response = requests.get("http://api.open-notify.org/astros.json")
            print(response)
            >>>> Response<200>
            
            response.content() # Return the raw bytes of the data payload
            response.text() # Return a string representation of the data payload
            response.json() # This method is convenient when the API returns JSON

*How to Use Query Parameters*
            
             query = {'lat':'45', 'lon':'180'}
             response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
             print(response.json())
        
*To run the web app:*

            $ python ./example.py
            * Running on http://127.0.0.1:5000/
            * Restarting with reloader
            
*cUrl commands for POST/DELETE/PUT requests*
        
            curl -i -H "Content-Type: application/json" -X DELETE  http://localhost:5000/httpbin/delete
            curl -i -H "Content-Type: application/json" -X POST  http://localhost:5000/httpbin/add
            curl -i -H "Content-Type: application/json" -X PUT  http://localhost:5000/httpbin/update


**References**
----------------------------------------------------------------------------------------------------------

- [Miguelgrinberg](https://blog.miguelgrinberg.com/)
- [Nylas](https://www.nylas.com/)
- [Dataquest](https://www.dataquest.io/)
- [Stackoverflow](https://stackoverflow.com/)