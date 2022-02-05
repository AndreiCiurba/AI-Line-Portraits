from turtle import *
import math
import random
import matplotlib
import matplotlib.pyplot as plt

def createInitial(points, numberOfKids):
    arrLength = 1
    width = 800
    height = 800
    r = 350
    px = []
    py = []
    pointArrayX =[]
    pointArrayY = []
    pointArrayX, pointArrayY = createPoints(points, px, py)
    # createImage(width, height)
    line_array_of_arrays = generateRandomArrays(numberOfKids, points, arrLength)
    for i in range(len(line_array_of_arrays)):
        crt_line_arr = line_array_of_arrays[i]
        plt.plot(pointArrayX, pointArrayY)
        plt.show()
    img_as_line_array = line_array_of_arrays
    return img_as_line_array

def continueMutating(mutated_line_array, points, numberOfKids):
    deleteImages()
    width = 800;
    height = 800;
    createImage(width, height)
    createPoints(points)
    for i in len(mutated_line_array):
        drawLines(line_array_of_arrays[i])
        saveImages(i, canvas)
        emptyCanvas()



def drawLines(line_array, pointArrayX, pointArrayY):
    pass


def createImage():
    pass
#
# def createCircularTemplate():
#     pass
#
# def createRectangularTemplate():
#     pass

def emptyCanvas():
    pass

def mutateImages():
    pass

def saveImage():
    pass

def deleteImages():
    pass




def createPoints(points,pointArrayX, pointArrayY, r = 350, x = 0, y = 0):
    for i in range(points):
        pointArrayX.append(x + r * math.cos(2 * math.pi * i/ points))
        pointArrayY.append(y + r * math.sin(2 * math.pi * i/ points))
    return pointArrayX, pointArrayY


def generateRandomArrays(numberOfKids, points, arrLength):
    return random.sample(range(0, points), arrLength)
