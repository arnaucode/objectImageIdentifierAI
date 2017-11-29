from os import walk
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps
import pandas as pd

#pixels, pixels of the output resizing images
size = 100, 100
def imgFileToData(path):
    image = Image.open(path)
    #resize the image
    thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_data = np.asarray(thumb)
    #.flatten()

    #check if the image had been resized to 100x100. 3pixels * 100width + 100 height = 30000
    if len(image_data)!=100:
        print("possible future ERROR!")
        print("len: " + str(len(image_data)))
        print("please, delete: " + path)
    return np.array(list(image_data))

def getDirectoryFiles(path, imgClass):
    images = []
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            #print(filename)
            image_data = imgFileToData(path + "/" + filename)
            images.append([image_data, imgClass])
            print(path + "/" + filename)
    return images


objects = getDirectoryFiles("object", 1)
noobjects = getDirectoryFiles("noobject", 0)

dataset = np.concatenate((objects, noobjects), axis=0)
#print(dataset[0])

np.save('dataset.npy', dataset)
'''
print(dataset)
np.savetxt('dataset.csv', dataset, delimiter=",", fmt='%d')

pd.set_option('display.max_colwidth', -1)
df = pd.DataFrame(dataset)
print(df.head())
print("aaa")
print(df[0][0])
print("aaa")
pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)
df.to_csv("dataset.csv", encoding='utf-8', index=False, header=False)
'''
