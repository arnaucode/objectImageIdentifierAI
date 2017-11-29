import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import os
from skimage import io

from skimage import color
from skimage import filters



def imgFileToData(path):
    image = Image.open(path)
    image_data = np.asarray(image)
    return image_data

def imgFileToData2(path):
    img = io.imread(path)
    return img

def detectObj(image_data):
    #image_data_blue = image_data[:,:,2]
    image_data_blue = color.rgb2grey(image_data)
    #image_data_blue = threshold(image_data)

    median_blue = np.median(image_data_blue)
    print median_blue
    median_blue = median_blue - median_blue/1.5
    print median_blue
    print image_data_blue

    non_empty_columns = np.where(image_data_blue.min(axis=0)<median_blue)[0]
    non_empty_rows = np.where(image_data_blue.min(axis=1)<median_blue)[0]

    boundingBox = (min(non_empty_rows), max(non_empty_rows), min(non_empty_columns), max(non_empty_columns))
    print boundingBox
    return boundingBox

def threshold(img):
    #img = color.rgb2grey(img)
    #img = img[:,:,2]
    img = color.rgb2grey(img)
    thresh = filters.threshold_mean(img)
    binary = img > thresh
    return binary

def prova(img):
    #return color.rgb2grey(img)
    return img

def crop(image_data, box):
    return image_data[box[0]:box[1], box[2]:box[3]]

def saveDataToImageFile(data, filename):
    image = Image.fromarray(data)
    image.save(filename)
