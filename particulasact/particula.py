from particulasact.algoritmos import distancia_euclidiana


class Particula:
    def __init__(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue, distancia=None):
        if distancia:
            self.creadorParticulas(id, origen_x, origen_y, destino_x,
                                   destino_y, velocidad, red, green, blue, distancia)

        else:
            self.__distancia = distancia_euclidiana(
                origen_x, origen_y, destino_x, destino_y)
            self.creadorParticulas(id, origen_x, origen_y, destino_x,
                                   destino_y, velocidad, red, green, blue, self.__distancia)

    def creadorParticulas(self, id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue, distancia):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__green = green
        self.__blue = blue
        self.__distancia = distancia

    @property
    def id(self):
        return self.__id

    @property
    def origen_x(self):
        return self.__origen_x

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def blue(self):
        return self.__blue

    @property
    def green(self):
        return self.__green

    @property
    def distancia(self):
        return self.__distancia

    def __str__(self):
        return f"Id: {self.__id}\nOrigen X: {self.__origen_x}\nOrigen Y: {self.__origen_y}\nDestino X: {self.__destino_x}\nDestino Y: {self.__destino_y}\nVelocidad: {self.__velocidad}\nRed: {self.__red}\nGreen: {self.__green}\nBlue: {self.__blue}\nDistancia: {self.__distancia}\n"

    def to_dict(self):
        return {
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "green": self.__green,
            "blue": self.__blue,
            "distancia": self.__distancia
        }
