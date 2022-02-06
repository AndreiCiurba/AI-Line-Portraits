import PIL.Image
import numpy as np
import math
import ai.algorithms as alg
import ai.utils as utils


def main():
    generation_size = 10
    number_of_kids = 12
    w = 10
    h = 10
    points = 24
    arr_length = 100


    utils.parseMainImg()
    main_img_path = "./images/mainImg/meFinal.png"
    main_image_final = utils.parseImg(main_img_path, w, h)


    utils.clearDb()
    print("Database initialized")
    alg.startGenerating(generation_size, number_of_kids,main_image_final, w, h, points, arr_length)

    
main()


## TODO: lookup Fail to create pixmap with Tk_GetPixmap in TkImgPhotoInstanceSetSize
## TODO: Remove all unused js stuff
