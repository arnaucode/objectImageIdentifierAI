echo "sending img1 to server"
echo "server response:"
curl -F file=@./test1.png http://127.0.0.1:3045/predict
echo ""


echo "sending img2 to server"
echo "server response:"
curl -F file=@./test2.png http://127.0.0.1:3045/predict
echo ""
