# imagesToDataset
Gets all the images from the directories 'object' and 'noobject', and puts in a dataset file.
The dataset file is a dataset.data file that contains 2 columns:
- images arrays of pixels
- 0 or 1, depending if is from the 'noobject' or 'object' directory


First, install the libraries.

### install scikit-learn
http://scikit-learn.org/stable/install.html
pip install -U scikit-learn

### install scikit-image
http://scikit-image.org/download
pip install -U scikit-image

### install numpy
https://www.scipy.org/install.html
python -m pip install --upgrade pip
pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

### install Pillow
http://pillow.readthedocs.io/en/3.0.x/installation.html
(sudo) pip install Pillow

### install matplotlib
https://matplotlib.org/users/installing.html
python -mpip install -U pip
python -mpip install -U matplotlib

may need to install python-tk:
sudo apt-get install python-tk


## to run
python readDataset.py
