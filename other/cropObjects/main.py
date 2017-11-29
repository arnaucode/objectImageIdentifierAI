from os import walk
import detectObject as do
import matplotlib.pyplot as plt



#image_data = do.imgFileToData("imgs/34.png")
image_data = do.imgFileToData2("object/25.png")


boundingBox = do.detectObj(image_data)
image_data = do.prova(image_data)
r = do.crop(image_data, boundingBox)


import detectObjects as dos
r_copy = r
dos.detectObjects(r_copy)
#do.saveDataToImageFile(image_data, "out.png")

#r = do.prova(image_data)

fig = plt.figure()
ax = fig.add_subplot(121)
ax.set_title("Original")
ax.imshow(image_data)

ax1 = fig.add_subplot(122)
ax1.set_title("Result")
ax1.imshow(r)

plt.show()

'''
f = []
for (dirpath, dirnames, filenames) in walk("imgs"):
    for filename in filenames:
        print filename
        image_data = do.imgFileToData("imgs/" + filename)
        boundingBox = do.detectObj(image_data)
        print boundingBox
'''
