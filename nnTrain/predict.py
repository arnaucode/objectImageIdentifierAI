from sklearn.neural_network import MLPClassifier
from skimage import io

img1 = io.imread("imgs/25.png")
img2 = io.imread("imgs/24.png")
img3 = io.imread("imgs/104.png")

img4 = io.imread("otherimgs/image_0008.jpg")


data_train = [img1, img2, img3, img4]
data_labels = [1, 1, 1, 0]
data_test = [img4, img3]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5,2), random_state=1)
clf.fit(data_train, data_labels)

clf.predict(data_test)

print "MPLClassifier values:"
[coef.shape for coef in clf.coefs_]



'''
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2, 4, index + 5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: %i' % prediction)
'''
