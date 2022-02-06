from turtle import *
import math
import random
import matplotlib
import matplotlib.pyplot as plt
import os
import glob
import shutil


def createInitial(points, number_of_kids, arr_length):
    px = []
    py = []
    point_array_x =[]
    point_array_y = []
    point_array_x, point_array_y = createPoints(points, px, py)
    # createImage(width, height)
    population = generateRandomArrays(number_of_kids, points, arr_length)
    for i in range(len(population)):
        px = []
        py = []
        individual = population[i]
        for j in range(arr_length):
            px.append(point_array_x[individual[j]])
            py.append(point_array_y[individual[j]])
        plotImage(px, py, i)
    return population

def continueMutating(mutated_population, points, number_of_kids, arr_length):
    deleteImages()
    px = []
    py = []
    point_array_x =[]
    point_array_y = []
    point_array_x, point_array_y = createPoints(points, px, py)
    for i in range(number_of_kids):
        px = []
        py = []
        individual = mutated_population[i]
        for j in range(arr_length):
            px.append(point_array_x[individual[j]])
            py.append(point_array_y[individual[j]])
        plotImage(px, py, i)



def plotImage(px, py, index):
    plt.figure(figsize=(8,8))
    plt.axis('off')
    plt.plot(px, py, 'k')
    path = "./images/children/test/image" + str(index) + ".png"
    plt.savefig(path, bbox_inches='tight', pad_inches=0)
    plt.close('all')
    plt.clf()



def deleteImages():
    shutil.rmtree("./images/children/test")
    os.mkdir("./images/children/test")


def createPoints(points, point_array_x, point_array_y, r = 350, x = 0, y = 0):
    for i in range(points):
        point_array_x.append(x + r * math.cos(2 * math.pi * i/ points))
        point_array_y.append(y + r * math.sin(2 * math.pi * i/ points))
    return point_array_x, point_array_y


def generateRandomArrays(number_of_kids, points, arr_length):
    return_array = []
    for i in range(number_of_kids):
        crt_arr = []
        for j in range(arr_length):
            crt_arr.append(random.randint(0, points - 1))
        return_array.append(crt_arr)
    return return_array
