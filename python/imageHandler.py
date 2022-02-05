import PIL.Image
import numpy as np
import math
import ai.algorithms as alg
import ai.utils as utils


def main():
    generationSize = 100
    numberOfKids = 24
    w = 40
    h = 40
    points = 96
    arrLength = 200

    mainImgPath = "./images/mainImg/me.png"
    image_array = utils.parseImg(mainImgPath, w, h)

    utils.clearDb()
    alg.startGenerating(generationSize, numberOfKids,image_array, w, h, points, arrLength)
main()


## TODO: lookup Fail to create pixmap with Tk_GetPixmap in TkImgPhotoInstanceSetSize
## TODO: Remove all unused js stuff
