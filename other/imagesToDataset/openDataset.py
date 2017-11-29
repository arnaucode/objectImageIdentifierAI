import matplotlib.pyplot as plt
import numpy as np
from random import randint



dataset = np.load('dataset.npy')

n = randint(0, len(dataset))

plt.plot(111)
plt.axis('off')
plt.imshow(dataset[n][0])
plt.title('class: ' + str(dataset[n][1]))

plt.show()
