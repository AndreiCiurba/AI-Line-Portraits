import PIL.Image
import numpy as np
import math
import ai.algorithms as alg
import ai.utils as utils


def main():
    generationSize = 2
    numberOfKids = 4
    w = 10
    h = 10
    points = 32

    mainImgPath = "./images/mainImg/me.png"
    image_array = utils.parseImg(mainImgPath, w, h)

    utils.clearDb()
    alg.startGenerating(generationSize, numberOfKids,image_array, w, h, points)

main()
