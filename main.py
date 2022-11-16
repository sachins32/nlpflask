import imp
import json
from flask import Flask, request, make_response
from logger import logger
import nlp as nlp
import numpy as np

logger.info("Starting the application")

app = Flask(__name__)
model = nlp.nlp_prediction()

@app.route("/", methods=["GET"])
def home():
    return "Ok"


@app.route("/predict", methods=["POST"])
def predict():
    content = request.json
    x = np.array(content)
    result = model.model_predict(content)
    print(f"result: {result}")
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')
