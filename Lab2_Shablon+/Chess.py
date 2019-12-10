from abc import ABCMeta, abstractmethod
import random


class Figure(metaclass=ABCMeta):  # Абстрактный класс фигура
    def __init__(self, name, color):
        self.figureName = name
        self.figureColor = color

    def gambit(self):
        self.move()
        flag = random.randint(0, 1)
        if flag:
            self.attack()
        else:
            self.death()

    def attack(self):
        print("Attack the figure")

    @abstractmethod
    def death(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def form(self):
        pass

    @abstractmethod
    def color(self):
        pass

class Pawn(Figure):  # Подкласс пешка с переопределением шагов алгоритма
    def move(self):
        print(self.figureName + " is moving + 1")

    def form(self):
        print("The " + self.figureName + " has helmet")

    def color(self):
        print(self.figureColor + " figure")

    def death(self):
        print("The " + self.figureName + " is eaten")


class Elephant(Figure):  # Подкласс слон с переопределением шагов алгоритма
    def move(self):
        print(self.figureName + " is moving diagonally")

    def form(self):
        print("The " + self.figureName + " has trunk")

    def color(self):
        print(self.figureColor + " figure")

    def death(self):
        print("The " + self.figureName + " is eaten")


if __name__ == '__main__':
    pawn = Pawn("Pawn", "White")
    elephant = Elephant("Elephant", "White")
    pawn.gambit()
    elephant.gambit()
    print(pawn.figureName)

