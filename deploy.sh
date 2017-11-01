timestamp() {
  date +"%T"
}


timestamp
echo "Starting imagesToDataset"
cd imagesToDataset && python main.py
cd ..
cp ./imagesToDataset/dataset.npy ./nnTrain/dataset.npy

timestamp
echo "Starting nnTrain"
cd nnTrain && python train.py
cd ..
cp ./nnTrain/nn.pkl ./serverPredictor/nn.pkl

timestamp
echo "Starting serverPredictor"
cd serverPredictor && python main.py


echo "----- deploy.sh finished -----"
timestamp
