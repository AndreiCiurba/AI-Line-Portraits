import PIL.Image
import numpy as np
import ai.utils as utils
import graphics.generator as generator
import random

def findErrorList(numberOfKids, w, h, main_image):
    errors = {}
    for kid in range(numberOfKids):
        path = "./images/children/test/image" + str(kid) + ".png"
        img_array_kid = utils.parseImg(path, w, h)
        errors[kid] = utils.calculateError(main_image,img_array_kid, w, h)
    return errors

def applyLineMutation(population, best_matches, arrLength):
    half_len = len(best_matches)
    new_population = []
    for i in range(half_len):
        new_population.append(population[best_matches[i]])
    for i in range(int(half_len/2)):
        interection = random.randint(0, arrLength - 1)
        father = new_population[2*i]
        mother = new_population[2*i + 1]
        kid_1 = father[:interection]
        kid_1.extend(mother[interection:])
        kid_2 = mother[:interection]
        kid_2.extend(father[interection:])
        new_population.append(kid_1)
        new_population.append(kid_2)
    return new_population



def startGenerating(generation_size, number_of_kids,main_image, w, h, points, arr_length):
    mutated_lines = []
    population = generator.createInitial(points, number_of_kids, arr_length)
    print("Population generated!")
    for generation in range(generation_size):
        errors_dict  = findErrorList(number_of_kids, w, h, main_image)
        print(errors_dict)
        best_matches = utils.selectBestMatches(errors_dict)
        print(best_matches)
        utils.writeToDb(errors_dict, best_matches, generation)
        mutated_population = applyLineMutation(population, best_matches, arr_length)
        print("Generation " + str(generation))
        generator.continueMutating(mutated_population, points, number_of_kids, arr_length)
        population = mutated_population

    print("Success!")
