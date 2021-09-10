
class Dog:

    def __init__(self, idade, nome):
        self.idade = idade
        self.nome = nome

    def age(self):
       print(self.idade)


dog = Dog(10, 'Fifi')

dog.age()
