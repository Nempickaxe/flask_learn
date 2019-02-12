
# coding: utf-8

# In[1]:


import pickle
from flask import Flask, request
import numpy as np
import pandas as pd
from flasgger import Swagger
import json


# In[2]:


with open('./model/rf.pkl', 'rb') as file:
    model = pickle.load(file)


# In[3]:


app = Flask(__name__)
swagger = Swagger(app)


# In[4]:


@app.route('/predict')
def prediction():
    """Example endpoint returning a prediction of iris
    ---
    parameters:
      - name: s_length
        in: query
        type: number
        required: true
      - name: s_width
        in: query
        type: number
        required: true
      - name: p_length
        in: query
        type: number
        required: true
      - name: p_width
        in: query
        type: number
        required: true
    """
    s_length = request.args.get('s_length')
    s_width = request.args.get('s_width')
    p_length = request.args.get('p_length')
    p_width = request.args.get('p_width')

    prediction = model.predict(np.array([[s_length, s_width, p_length, p_width]]))
    return str(prediction)


# In[5]:


@app.route('/predict_file', methods=["POST"])
def predict_iris_file():
    """Example file endpoint returning a prediction of iris
    ---
    parameters:
      - name: input_file
        in: formData
        type: file
        required: true
    """
    input_data = pd.read_csv(request.files.get("input_file"), header=None)
    prediction = model.predict(input_data)
    return str(list(prediction))


# In[6]:


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
