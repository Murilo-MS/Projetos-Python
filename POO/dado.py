
import random

class Dado:

    def __init__(self, lados):
        print("Contruindo dado de {} faces!".format(lados))
        self.__lados = lados
        self.lista = []

    def faces(self):
        #lista = []
        for i in range(self.__lados):
            self.lista.append(i + 1)
        print(self.lista)

    def rolar(self, vezes):
        for j in range(vezes):
            print(random.choice(self.lista))

