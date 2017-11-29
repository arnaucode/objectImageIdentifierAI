echo "sending img1 to server"
echo "server response:"
curl -X POST -F file=@./test1.png http://127.0.0.1:3000/predict
echo ""

echo "sending img2 to server"
echo "server response:"
curl -X POST -F file=@./test2.png http://127.0.0.1:3000/predict
echo ""

echo "sending img to server"
echo "server response:"
curl -X POST -F file=@./test3.png http://127.0.0.1:3000/predict
echo ""
