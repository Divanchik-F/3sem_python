# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    _health=100
    _attack=50
    _experience=0

    def __init__(self, name):
        self._name=name

    def attack(self, target):
        target._health-=self._attack
        self._experience+=1

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
