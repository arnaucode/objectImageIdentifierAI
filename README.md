# objectImageIdentifierAI

- imagesToDataset
    - From two directories ('object' and 'noobject'), gets all the images inside the directories and generates the dataset
- nnTrain
    - From the dataset file generated in the previous step, train the Neural Network
- serverPredictor
    - Runs a server API, that with the Neural Network classifies the incoming images
- smartphoneApp
    - Take photo and upload to the server, to get the response (object or no object)

![hotdognohotdog](https://raw.githubusercontent.com/arnaucode/objectImageIdentifierAI/master/hotdognohotdog.png "hotdognohotdog")


## Real steps
- download images
    - for example, can be done with https://github.com/arnaucode/imgDownloader.git
- In /serverPredictor directory
```
python classifierChooser.py
```
This will generate the model.pkl. Then, run the serverPredictor.py
```
python serverPredictor.py
```
