import PIL.Image
import numpy as np
import ai.utils as utils
import myTurtle.generator as generator


def firstAttemptAI(numberOfKids, w, h, image_array):
    errors = {}
    for kid in range(numberOfKids):
        path = "./images/children/img" + str(kid) + ".png"
        img_array_kid = utils.parseImg(path, w, h)
        errors[kid] = utils.calculateError(image_array,img_array_kid, w, h)
    return errors

def applyLineMutation(img_as_line_array, best_matches):
    ## TODO: fix it
    l = len(best_matches)
    return img_as_line_array[:l]




def startGenerating(generationSize, numberOfKids,image_array, w, h, points):
    # mutated_lines = []
    # img_as_line_array = generator.createInitial(points, numberOfKids)
    # for generation in range(generationSize):
    #     errors_dict  = firstAttemptAI(numberOfKids, w, h, image_array)
    #     best_matches = utils.selectBestMatches(errors_dict)
    #     utils.writeToDb(errors_dict, best_matches, generation)
    #     mutated_lines = applyLineMutation(img_as_line_array, best_matches)
    #     generator.continueMutating(mutated_lines, points, numberOfKids)
    generator.createInitial(points, numberOfKids)
    print("Success!")
