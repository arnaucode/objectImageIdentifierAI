# serverImgPredictor
Need the file dataset.data

### install Flask
http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
(sudo) pip install Flask

pip install flask_restful
pip install flask-jsonpify

### install scikit-neuralnetwork
https://scikit-neuralnetwork.readthedocs.io/en/latest/guide_installation.html
pip install scikit-neuralnetwork

also need to upgrade the Lasagne library:
(sudo) pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip


## Run
python train.py

will generate nn.pkl

copy nn.pkl to the serverPredictor directory
