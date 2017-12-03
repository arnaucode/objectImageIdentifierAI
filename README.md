# objectImageIdentifierAI


## Run
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
- Can run the tests:
```
bash test.sh
```
- The deploy.sh will execute the classifierChooser.py, and then the serverPredictor.py
```
bash deploy.sh
```



![hotdognohotdog](https://raw.githubusercontent.com/arnaucode/objectImageIdentifierAI/master/hotdognohotdog.png "hotdognohotdog")
