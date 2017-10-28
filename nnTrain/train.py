import matplotlib.pyplot as plt
import numpy as np
from random import randint
import pickle
from sknn.mlp import Classifier, Layer, Convolution

def datasetToTrainAndTestData(dataset, numtest):
    np.random.shuffle(dataset)
    print "length total data:" + str(len(dataset))

    traindata = np.copy(dataset)
    testdata = []
    for i in range(numtest):
        #get random integer between 0 and the total amount of images in the dataset
        n = randint(0, len(traindata))
        testdata.append(dataset[n])

        #delete the n image (dataset[n]) of the traindata
        traindata = np.delete(traindata, n, axis=0)
    testdataNP = np.array(testdata)
    return traindata, testdataNP


#read the dataset made with the 'imagesToDataset' repository
dataset = np.load('dataset.npy')

traindata, testdata = datasetToTrainAndTestData(dataset, 10)
print "length traindata: " + str(len(traindata))
print "length testdata: " + str(len(testdata))

#traindataAttributes contains all the pixels of each image
traindataAttributes = traindata[:,0]
traindataAttributes = np.array([[row] for row in traindataAttributes])

#traindataLabels contains each label of each image
traindataLabels = traindata[:,1]
traindataLabels = traindataLabels.astype('int')

#testdataAttributes contains the pixels of the test images
testdataAttributes = testdata[:,0]
testdataAttributes = np.array([[row] for row in testdataAttributes])

#testdataLabels contains each label of each image
testdataLabels = testdata[:,1]
testdataLabels = testdataLabels.astype('int')

#default: units=100, learning_rate=0.001, n_iter=25
nn = Classifier(
    layers=[
        Layer("Sigmoid", units=10),
        Layer("Softmax")],
    learning_rate=0.001,
    n_iter=20,
    verbose=True)

nn.fit(traindataAttributes, traindataLabels)

print('\nTRAIN SCORE', nn.score(traindataAttributes, traindataLabels))
print('TEST SCORE', nn.score(testdataAttributes, testdataLabels))

#save the neural network configuration
pickle.dump(nn, open('nn.pkl', 'wb'))
