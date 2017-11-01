from os import walk
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageOps

#pixels, pixels of the output resizing images
size = 100, 100
def imgFileToData(path):
    image = Image.open(path)
    #resize the image
    thumb = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_data = np.asarray(thumb).flatten()
    '''
    plt.plot(111)
    plt.imshow(thumb)
    plt.show()
    '''
    if len(image_data)!=30000:
        print "possible future ERROR!"
        print "len: " + str(len(image_data))
        print "please, delete: " + path
    return image_data

def getDirectoryFiles(path, imgClass):
    images = []
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            #print filename
            image_data = imgFileToData(path + "/" + filename)
            images.append([image_data, imgClass])
            print path + "/" + filename
    return images


def asdf():
    for index, (image, prediction) in enumerate(images_and_predictions[:4]):
        plt.subplot(2, 4, index + 5)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Prediction: %i' % prediction)


objects = getDirectoryFiles("object", 1)
noobjects = getDirectoryFiles("noobject", 0)

dataset = np.concatenate((objects, noobjects), axis=0)

np.save('dataset.npy', dataset)
