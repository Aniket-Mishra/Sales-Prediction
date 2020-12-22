import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    # get data
    features = [np.array([int(x) for x in request.form.values()])]

    prediction = model.predict(features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text = 'The Sales in Month 3 should be $ {}'.format(output))

if __name__ == '__main__':
    app.run(debug = True)