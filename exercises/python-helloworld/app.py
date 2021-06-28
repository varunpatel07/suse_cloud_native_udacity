import json
from flask import Flask, render_template 
import logging
app = Flask(__name__,template_folder='template')

@app.route('/logs')
def log():
    with open(r'D:\udacity\exercises\python-helloworld\app.log', 'r') as f: 
        return render_template('logs.html', text=f.read()) 

@app.route("/")
def hello():
    #app.logger.info("MAIN CALLED")
    logging.debug("Main called")

    return "Hello World!"

@app.route("/status")
def status():
    #app.logger.info("STATUS CALLED")
    logging.info("status called")
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),

    )
    return response

@app.route("/metric")
def metric():
    #app.logger.info("METRIC CALLED")
    logging.info("metrics called")
    response=app.response_class(
        response=json.dumps({"data":{"UserCount":200,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
        )
    return response



if __name__ == "__main__":
    handler=[logging.FileHandler(r'D:\udacity\exercises\python-helloworld\app.log'),logging.StreamHandler()]
    logging.basicConfig(level=logging.INFO,handlers=handler)
    app.debug=True  
    app.run(host='0.0.0.0')
