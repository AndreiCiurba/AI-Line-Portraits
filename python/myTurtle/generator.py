from turtle import *
import math
import random
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
import shutil


def createInitial(points, numberOfKids, arrLength):
    px = []
    py = []
    pointArrayX =[]
    pointArrayY = []
    pointArrayX, pointArrayY = createPoints(points, px, py)
    # createImage(width, height)
    line_array_of_arrays = generateRandomArrays(numberOfKids, points, arrLength)
    for i in range(len(line_array_of_arrays)):
        px = []
        py = []
        crt_line_arr = line_array_of_arrays[i]
        for j in range(arrLength):
            px.append(pointArrayX[crt_line_arr[j]])
            py.append(pointArrayY[crt_line_arr[j]])
        plt.figure(figsize=(8,8))
        plt.axis('off')
        plt.plot(px, py, 'k')
        path = "./images/children/test/image" + str(i) + ".png"
        plt.savefig(path, bbox_inches='tight', pad_inches=0)
        plt.clf()
        plt.close('all')
    img_as_line_array_of_arrays = line_array_of_arrays
    return img_as_line_array_of_arrays

def continueMutating(mutated_line_array_of_arrays, points, numberOfKids,arrLength):
    deleteImages()
    px = []
    py = []
    pointArrayX =[]
    pointArrayY = []
    pointArrayX, pointArrayY = createPoints(points, px, py)
    for i in range(len(mutated_line_array_of_arrays)):
        px = []
        py = []
        mutated_line_array = mutated_line_array_of_arrays[i]
        for j in range(arrLength):
            px.append(pointArrayX[mutated_line_array[j]])
            py.append(pointArrayY[mutated_line_array[j]])
        plt.figure(figsize=(8,8))
        plt.axis('off')
        plt.plot(px, py, 'k')
        path = "./images/children/test/image" + str(i) + ".png"
        plt.savefig(path, bbox_inches='tight', pad_inches=0)
        plt.close('all')
        plt.clf()

def deleteImages():
    shutil.rmtree("./images/children/test")
    os.mkdir("./images/children/test")


def createPoints(points,pointArrayX, pointArrayY, r = 350, x = 0, y = 0):
    for i in range(points):
        pointArrayX.append(x + r * math.cos(2 * math.pi * i/ points))
        pointArrayY.append(y + r * math.sin(2 * math.pi * i/ points))
    return pointArrayX, pointArrayY


def generateRandomArrays(numberOfKids, points, arrLength):
    returnArray = []
    for i in range(numberOfKids):
        crtArr = []
        for j in range(arrLength):
            crtArr.append(random.randint(0, points -1))
        returnArray.append(crtArr)
    return returnArray
