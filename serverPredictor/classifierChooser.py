from PIL import Image, ImageOps
import numpy, os

from sklearn.feature_extraction import image
from sklearn.model_selection import KFold, cross_val_score

import numpy as np
import pandas as pd
from time import time
import pickle

from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV


path="dataset/"
Xlist=[]
Ylist=[]
size = 100, 100

#load images from dataset
for directory in os.listdir(path):
    for file in os.listdir(path+directory):
        print(path+directory+"/"+file)
        img=Image.open(path+directory+"/"+file)
        #resize
        thumb = ImageOps.fit(img, size, Image.ANTIALIAS)
        image_data = np.array(thumb).flatten()[:100]
        Xlist.append(image_data)
        Ylist.append(directory)

from sklearn.ensemble import RandomForestClassifier

pipe = Pipeline([
        ('clf', RandomForestClassifier()),
    ])

param_grid = dict(clf__n_estimators=[100])

grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=-1, verbose=1, cv=3)

# Utility function to report best scores
def report(results, n_top=10):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                  results['mean_test_score'][candidate],
                  results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")

start = time()
grid_search = GridSearchCV(pipe, param_grid, n_jobs=-1, verbose=1, cv=3)
grid_search.fit(Xlist, Ylist)
print("GridSearchCV took %.2f seconds for %d candidate parameter settings."
      % (time() - start, len(grid_search.cv_results_['params'])))
print("finished GridSearch")
report(grid_search.cv_results_)

pickle.dump(grid_search, open('model.pkl', 'wb'))
print("pipeline model saved to model.pkl")
