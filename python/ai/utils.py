import math
import PIL.Image
from PIL import ImageDraw
import numpy as np

def parseMainImg():
    #THANK YOU STACKOVERFLOW!!!
    img=PIL.Image.open("./images/mainImg/me.png").convert("RGB")
    npImage=np.array(img)
    h,w=img.size
    alpha = PIL.Image.new('L', img.size,0)
    draw = ImageDraw.Draw(alpha)
    draw.pieslice([0,0,h,w],0,360,fill=255)
    npAlpha=np.array(alpha)
    npImage=np.dstack((npImage,npAlpha))
    PIL.Image.fromarray(npImage).save('./images/mainImg/meFinal.png')


def parseImg(path, w, h):
    image = PIL.Image.open(path).convert('L')
    image.thumbnail(size=(w, h))
    image_array = list(np.array(image))
    return image_array

def selectBestMatches(dict):
    dict = sorted(dict.items(), key=lambda x: x[1])
    best_matches = [x[0] for x in dict]
    return best_matches[:int(len(best_matches)/2)]

def calculateError(image_array,img_array_kid,w,h):
    error = 0
    for i in range(w):
        for j in range(h):
            error = error + abs(int(image_array[i][j]) - int(img_array_kid[i][j]))
    return error

def writeToDb(dictionary, matches, generation):
    f = open("./rudimentary_database.txt", "a")
    f.write("Generation: " + str(generation) + "\n")
    f.write("Best match error: " + str(dictionary[matches[0]]) + "\n")
    f.write("See picture (not yet implemented): image" + str(matches[0]) + ".png" + "\n\n")
    f.close()
    saveBestImg()

def clearDb():
    f = open("./rudimentary_database.txt", "w")
    f.write("")
    f.close()

def saveBestImg():
    pass
