# -*- coding: utf-8 -*-
import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('heartass.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    Age = int(request.args.get('age'))
    
    prediction =int(model.predict([[exp]]))
    
        
    return render_template('index.html', prediction_text='Regression Model  has predicted heart attack possibility for given age and gender: {}'.format(prediction))





if __name__ == "__main__":
    app.run(debug=True)
