from flask import Flask
from flask_restful import Resource, Api, request

import matplotlib.pyplot as plt
import numpy as np
import cv2
import io
from PIL import Image, ImageOps

import pickle

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 16 MB
api = Api(app)

size = 100, 100


#load Neural Network, generated with nnTrain
nn = pickle.load(open('nn.pkl', 'rb'))

class Predict(Resource):
    def get(self):
        message = {'message': 'getted route1'}
        return message
    def post(self):
        filer = request.files['file']
        #open the uploaded image, and transform to the numpy array
        filer.save("currentimage.png")
        image = Image.open("currentimage.png")
        thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_data = np.asarray(thumb).flatten()
        imagetopredict = np.array([image_data])

        #predict the class of the image with the neural network
        prediction = nn.predict(imagetopredict)
        print "prediction"
        print prediction[0][0]
        if prediction[0][0]==0:
            result = "noobject"
        else:
            result = "object"
        message = {'class': result}
        return message


class Route2(Resource):
    def get(self):
        return {'message': 'getted route2'}


class Route3(Resource):
    def get(self):
        return {'message': 'getted route3'}


api.add_resource(Predict, '/predict')
api.add_resource(Route2, '/route2')
api.add_resource(Route3, '/route3')


if __name__ == '__main__':
     app.run(port='3045')
