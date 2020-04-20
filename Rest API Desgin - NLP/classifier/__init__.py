from typing import Tuple
from os import path
import os
import csv
from json import loads
import json
import pandas as pd
from numpy import ndarray, array, append
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from scipy.sparse.csr import csr_matrix
import joblib
from pandas.io.json import json_normalize
import warnings

warnings.filterwarnings("ignore", category=FutureWarning)

def load(directory: str = '../data'):
    """Load in the data
    """
    # Type annotations for readability
    unified_data: ndarray

    # File paths for reading data
    txt_path = path.join(directory, 'data.txt')
    supl_path = path.join(directory, 'supplemental_data.json')
    # TODO: Add your data retrieval code - Done
    # Your Data Retrieval Code #

    ##converting json to dataframe

    # File Read 1: Reading the first file.
    with open(supl_path) as json_file:
        data = json.load(json_file)
    df1 = json_normalize(data)
    df1 = df1.rename(columns={"EventType": "EventClass"})

    # File Read 2: reading the text file
    df2 = pd.read_csv(txt_path, sep='\t')

    # appending both the dataframe
    result = df1.append(df2)
    #rotating the dataframe and trasforming to numpy array
    unified_data = result.T.to_numpy()

    # End Your Data Retrieval Code #

    # Type check for output
    if not isinstance(unified_data, ndarray):
        raise TypeError('unifieddata must by a numpy ndarray type')
    if unified_data.shape != (2, 287):
        raise ValueError('Incorrect shape for unified data')

    return unified_data

def build_vectorize() -> Tuple[ndarray, csr_matrix, CountVectorizer]:
    """Construct and return a vectorizer
    """
    # Type annotations for readability
    vectorizer: CountVectorizer
    fit_array: csr_matrix
    unified_data: ndarray

    # Retrieve data
    unified_data = load()

    # TODO: Add your vectorizer - Done
    # Your Vectorizer #

    vectorizer = CountVectorizer()
    fit_array = vectorizer.fit_transform(unified_data[1])

    # End Your Vectorizer #

    # Type check for output
    if not isinstance(fit_array, csr_matrix):
        raise TypeError('Fit array must be a scipy csr sparse matrix')
    if not isinstance(vectorizer, CountVectorizer):
        raise TypeError('vectorizer must be a class or subclass of CountVectorizer (includes TFIDF vectorizers')

    return unified_data, fit_array, vectorizer

def train() -> Tuple[str, str]:
    """

    """
    # Type annotations for readability
    vectorizer: CountVectorizer
    fit_array: csr_matrix
    unified_data: ndarray
    model: LogisticRegression

    unified_data, fit_array, vectorizer = build_vectorize()

    # TODO: Your model goes here
    # Your Model Here #
    # print(unified_data[1])
    print(fit_array)
    X_train, X_test, y_train, y_test = train_test_split(fit_array, unified_data[0], random_state=0,test_size=0.3)
    logreg = LogisticRegression()
    model = logreg.fit(X_train, y_train)

    # Use score method to get accuracy of model
    score = model.score(X_test, y_test)
    print(score)

    # End Your Model#

    # Serialize models
    # TODO: no directory named serializedmodels
    model_location = 'serializedmodels/model.joblib'
    vectorizer_location = 'serializedmodels/vectorizer.joblib'
    joblib.dump(model, model_location)
    joblib.dump(vectorizer, vectorizer_location)

    return model_location, vectorizer_location

def classify(text: str, model: LogisticRegression = None, vectorizer: CountVectorizer = None) -> str:
    """This classify function should take in a string text parameter
    and return the category for which it's most likely classified as
    a string.
    """
    # Type annotations for readability
    vectorizer: CountVectorizer
    model: LogisticRegression
    result: str

    if not model:
        model = joblib.load('serializedmodels/model.joblib')
    if not vectorizer:
        vectorizer = joblib.load('serializedmodels/vectorizer.joblib')
    if not isinstance(text, str):
        raise TypeError('Text must be a string')

    if len(text) == 0:
        return 'No prediction'
    text_transformed = vectorizer.transform([text])

    # TODO: Return the most likely category in the constraints of the README
    # Your Prediction Block


    if (not (model.predict_proba(text_transformed)>0.25).any()): ## check if there is no value greater than 0.25
        result = ''
    else:
        result = model.predict(text_transformed)

    # result = ''
    # End Prediction Block
    return result


