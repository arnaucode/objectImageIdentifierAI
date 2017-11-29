import pandas as pd
import logging
from datetime import datetime
import time
import os

import pickle
import numpy as np


from flask import Flask
from flask_restful import Resource, Api, request


from PIL import Image, ImageOps

#image size after resize
size = 100, 100

#model = pickle.load(open('model.pkl', 'rb'))
#print('model loaded')



app = Flask(__name__)
api = Api(app)


class Predict(Resource):
    def post(self):
        print("new predict")
        start = time.time()
        filer = request.files['file']#open the uploaded image, and transform to the numpy array

        #process the img
        filer.save("currentimage.png")
        image = Image.open("currentimage.png")
        thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
        image_data = np.array(thumb).flatten()[:100]

        #load the selected model
        model = pickle.load(open('model.pkl', 'rb'))
        print('model.pkl loaded')

        #predict with the selected model
        r = model.predict([image_data])[0]

        logging.info("  [result]: " + r)
        roundtrip = time.time() - start
        logging.info("  [roundtriptime]: " + str(roundtrip) + "s")
        return({'result': r})

api.add_resource(Predict, '/predict')


if __name__ == '__main__':
    log_directory = 'log'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    logfilename = log_directory + "/logging"+ datetime.now().strftime("%Y-%M-%d-%H:%m:%s") + ".log"
    logging.basicConfig(filename=logfilename,level=logging.DEBUG)

    print("server running")
    app.run(port='3000')
