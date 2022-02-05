import PIL.Image
import numpy as np
import ai.utils as utils
import myTurtle.generator as generator
import random

def firstAttemptAI(numberOfKids, w, h, image_array):
    errors = {}
    for kid in range(numberOfKids):
        path = "./images/children/test/image" + str(kid) + ".png"
        img_array_kid = utils.parseImg(path, w, h)
        errors[kid] = utils.calculateError(image_array,img_array_kid, w, h)
    return errors

def applyLineMutation(img_as_line_array_of_arrays, best_matches, arrLength):
    half_len = len(best_matches)
    print(best_matches)
    new_line_array_of_arrays = img_as_line_array_of_arrays[:half_len]
    for i in range(int(half_len/2)):
        interection = random.randint(0, arrLength -1)
        father = img_as_line_array_of_arrays[2*i]
        mother = img_as_line_array_of_arrays[2*i + 1]
        kid_1 = father[:interection]
        kid_1.extend(mother[interection:])

        kid_2 = mother[:interection]
        kid_2.extend(father[interection:])
        new_line_array_of_arrays.append(kid_1)
        new_line_array_of_arrays.append(kid_1)
    return new_line_array_of_arrays



def startGenerating(generationSize, numberOfKids,image_array, w, h, points, arrLength):
    mutated_lines = []
    img_as_line_array_of_arrays = generator.createInitial(points, numberOfKids, arrLength)

    for generation in range(generationSize):
        errors_dict  = firstAttemptAI(numberOfKids, w, h, image_array)
        best_matches = utils.selectBestMatches(errors_dict)
        utils.writeToDb(errors_dict, best_matches, generation)
        mutated_lines = applyLineMutation(img_as_line_array_of_arrays, best_matches, arrLength)
        print("Generation " + str(generation))
        generator.continueMutating(mutated_lines, points, numberOfKids, arrLength)
    print("Success!")
