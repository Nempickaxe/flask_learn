from keras.models import load_model
import pandas as pd, numpy as np
from PIL import Image
from flasgger import Swagger
from flask import Flask, request

app = Flask(__name__)
swagger = Swagger(app)

model = load_model('./model.h5')

@app.route('/predict_digit', methods=['POST'])
def predict_digit():
    """
    Example Endpoint returning prediciton of MNIST
    ---
    parameters:
        - name: image
          in: formData
          type: file
          required: true
    """
    im = Image.open(request.files['image'])
    im2arr = np.array(im).reshape((1,1,28,28))
    return str(np.argmax(model.predict(im2arr)))

if __name__=='__main__':
    app.run('localhost', port=5000)

