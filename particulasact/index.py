import json
from particulasact.particula import Particula


class Nodo():
    dato = None
    siguiente = None
    anterior = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista_ligada():

    def __init__(self):
        self.nodo_inicial = None
        self.nodo_final = None
        self.no_elements = 0

    def __str__(self):
        temp = self.nodo_inicial
        array = []
        while(temp):
            array.append(str(temp.dato))
            temp = temp.siguiente
        return "".join(array)

    def __len__(self):
        return self.no_elements

    def __iter__(self):
        self.itertemp = self.nodo_inicial
        return self

    def __next__(self):
        if(self.itertemp):
            temp = self.itertemp.dato
            self.itertemp = self.itertemp.siguiente
            return temp
        else:
            raise StopIteration

    def agregar_inicio(self, nodo):
        if(self.no_elements == 0):
            self.nodo_inicial = nodo
            self.nodo_final = nodo
            self.no_elements = self.no_elements + 1
        else:
            temporal = self.nodo_inicial
            temporal.anterior = nodo
            nodo.siguiente = temporal
            self.nodo_inicial = nodo
            self.no_elements = self.no_elements + 1

    def agregar_final(self, nodo):
        if(self.no_elements == 0):
            self.nodo_inicial = nodo
            self.nodo_final = nodo
            self.no_elements = self.no_elements + 1
        else:
            temporal = self.nodo_final
            temporal.siguiente = nodo
            nodo.anterior = temporal
            self.nodo_final = nodo
            self.no_elements = self.no_elements+1

    def mostrar(self):
        temp = self.nodo_inicial
        while(temp):
            print(temp.dato)
            temp = temp.siguiente

    def guardar(self, ubicacion):
        temp = self.nodo_inicial
        try:
            with open(ubicacion, 'w') as archivo:
                lista = []
                while(temp):
                    lista.append(temp.dato.to_dict())
                    temp = temp.siguiente
                json.dump(lista, archivo, indent=1)
            return 1

        except:
            return 0

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                for particula in lista:
                    particulaNodo = Particula(**particula)
                    nodo = Nodo(particulaNodo)
                    self.agregar_final(nodo)
            return 1

        except:
            return 0
