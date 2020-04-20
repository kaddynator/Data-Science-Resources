from typing import List, Dict
from flask import jsonify, request

from app.api import api
from classifier import classify
import joblib

VECTORIZER = joblib.load(
    "classifier/serializedmodels/vectorizer.joblib")
MODEL = joblib.load(
    'classifier/serializedmodels/model.joblib')


@api.route('/classify', methods=['GET'])  # local:5000/classify
def _classify():
    """Get endpoint to classify text. Expects application/json as content type.
    Expects the json to follow structure {"text": ["sentence to class 1", "sentence 2", ...]}
    """
    # Validate content type
    if not request.content_type.startswith('application/json'):
        raise TypeError('Request content type must be of application/json')
    request_data: Dict = request.json

    # Validate required json fields
    if 'text' not in request_data:
        raise ValueError('Missing required json attribute "text" in json call')
    to_classify: List[str] = request_data['text']

    # Validate contents of text to classify
    if not isinstance(to_classify, list):
        raise TypeError('Data provided in "text" must be a list')
    if not all([isinstance(x, str) for x in to_classify]):
        raise TypeError('List of instances contains non-string inputs')

    # TODO: Explain why the classify function is supplied the MODEL and VECTORIZER global objects from lines 7 and 8 instead of using the defaults?
    results: List[str] = [classify(x, model=MODEL, vectorizer=VECTORIZER) for x in to_classify]

    # Check that we have full results for each item
    if len(results) != len(to_classify):
        raise ValueError('Result length does not match request length')

    return jsonify(results)
