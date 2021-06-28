import json
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),

    )
    return response

@app.route("/metric")
def metric():
    response=app.response_class(
        response=json.dumps({"data":{"UserCount":200,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
        )
    return response

if __name__ == "__main__":
    app.debug=True  
    app.run(host='0.0.0.0')
