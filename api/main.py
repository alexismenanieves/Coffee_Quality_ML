from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import traceback
import pickle

app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict/feature1/feature2/feature3/feature4/feature5/feature6/feature7/feature8/', methods=['POST']) # Your API endpoint URL would consist /predict
def predict():

    country_of_origin = str(feature1)
    variety = str(feature2)
    aroma = float(feature3)
    aftertaste = float(feature4)
    acidity = float(feature5)
    body = float(feature6)
    balance = float(feature7)
    moisture = float(feature8)

    pred_array = np.array([[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]])
    df_api = pd.DataFrame(data=pred_array, columns=['country_of_origin','variety','aroma','aftertaste','acidity','body','balance','moisture'])

    try:
        prediction = list(model.predict(df_api))
        return jsonify({'prediction': prediction})

    except:
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    filename = '../model/coffee_model.pkl'
    model = pickle.load(open(filename,'rb'))
    app.run(debug=True)