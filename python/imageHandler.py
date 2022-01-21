import PIL.Image
import numpy as np
import math

generationSize = 1
numberOfKids = 1
w = 40
h = 40

errors = []

image = PIL.Image.open("./images/mainImg/me.png").convert('L')
image.thumbnail(size=(w, h))
image_array = np.array(image)
rows = int(math.sqrt(image_array.size))
columns = int(math.sqrt(image_array.size))
image_array = list(image_array)
# for line in image_array :
#     print ('  '.join(map(str, line)))
for i in range(rows):
    for j in range(columns):
        print(image_array[i][j], end =" ")
    print()

# read all images from folder

print()

for i in range(generationSize):
    errors = []
    for j in range(numberOfKids):
        #read image
        path = "./images/children/img" + str(i) + ".png"
        image2 = PIL.Image.open(path).convert('L')
        image2.thumbnail(size=(w, h))
        #turn to matrix
        img_array_kid = np.array(image2)
        img_array_kid = list(img_array_kid)
        #calculateError
        error = 0
        for i in range(rows):
            for j in range(columns):
                error = error + abs(image_array[i][j] - img_array_kid[i][j])

        for i in range(rows):
            for j in range(columns):
                print(img_array_kid[i][j], end =" ")
            print()
        errors.append(error)
    print(errors)





    <# TODO: remove all javascript and replace with turtle or matplotlib
