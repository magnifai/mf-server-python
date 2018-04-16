from flask import Flask
import json

from util import validate_args, is_authorized
from ../src/main import get_data

app = Flask(__name__)

@app.route("/")
def hello():
    return "Ok"

@app.route("/health")
def health():
    return "Ok"

@app.route("/data") # TODO: more descriptive name
def data(args):
    # TODO: add better error handling
    validate_args(args)
    
    api_key = args["api_key"]

    is_authorized(api_key)

    return json.dumps({
        data: get_data(params)
    })

