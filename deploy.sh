timestamp() {
  date +"%T"
}

cd serverPredictor

timestamp
echo "Starting training the model: classifierChooser.py"
python classifierChooser.py

timestamp
echo "Starting serverPredictor"
xterm -hold -e 'python serverPredictor.py' &

sleep 4

timestamp
echo "Starting test.sh"
xterm -hold -e 'bash test.sh' &
