import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')

def predict():

    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    prediction = model.predict(data_df)

    output = round(prediction[0], 2) # [0] is the predicted value of the model. a model returns many values.

    final_output = {'results': output}

    return jsonify(results = final_output)


if '__name__' == '__main__':
    app.run(port = 5000, debug = True)