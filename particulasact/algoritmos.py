import math


def distancia_euclidiana(x_1, y_1, x_2, y_2):
    return "{:.5f}".format(math.sqrt(math.pow((x_2-x_1), 2)+math.pow(y_2-y_1, 2)))
