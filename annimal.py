import  abc
class Animal(abc.ABC):
    nmbr = 0

    def __init__(self, nom_ac:str, espece_ac:str):
        self.nom_a = nom_ac
        self.espece = espece_ac
        self.nmbr +=1

    def parler(self,):
        pass

class Chien(Animal):

    def __init__(self,nom, espece ):
        super().__init__(nom, espece)

    def parler(self,):
        return "woof"



#  instancier de la classe

c1 = Chien(name="chien policier",espece= "Mamifer")

print(c1.nom_a)
print(c1.espece)

print(c1.parler())


