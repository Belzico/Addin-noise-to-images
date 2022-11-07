import numpy as np
import cv2 as cv
import random
from skimage import io
from wand.image import wand_image

# funtion salt and pepper noise
def sp_noise(image, value):
    
    temp=value
    while type(temp)==tuple:
        temp=value[0]
    prob=temp
    result = np.zeros(image.shape, np.uint8)

    thres = 1-prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rnd = random.random()

            # Cambio por sal
            if rnd < prob:
                result[i][j] = 0
            # Cambio por pimienta
            elif rnd > thres:
                result[i][j] = 255
            # Sin cambio
            else:
                result[i][j] = image[i][j]

    return result


def escala_grises(image, *args):

    matriz = np.zeros((image.shape[0], image.shape[1]), np.uint8)

    for i in range(matriz.shape[0]):
        for j in range(matriz.shape[1]):
            # El doble / es para dividir y redondear a entero
            promedio = (image[i][j][0] + image[i][j][1] + image[i][j][2])//3
            matriz[i][j] = promedio
    return matriz



# Import Image from wand.image module
def wand_laplacian(image, *args):

# Read image using Image() function
    result=wand_image(image)


    # Generate noise image using spread() function
    result.noise("laplacian", attenuate = 1.0)
    return result
