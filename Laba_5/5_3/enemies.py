# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy

def generate_random_troll():
    RandomEnemyType = choice(troll_types)
    enemy = RandomEnemyType()
    return enemy

def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

def generate_troll_list(enemy_number):
    enemy_list = [generate_random_troll() for i in range(enemy_number)]
    return enemy_list

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1, 100)
        y = randint(1, 100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

    def question(self):
        x = randint(1, 20)
        y = randint(1, 20)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer=answer

    def get_answer(self):
        return self.__answer

    def check_answer(self, answer):
        return answer==self.__answer

class WhiteTroll(Troll):
    def __init__(self):
        self._health=50
        self._attack=10
        self._color='белый'

    def question(self):
        x=randint(1, 5)
        self.__quest="Угадай число от 1 до 5"
        self.set_answer(x)
        return self.__quest

class BlueTroll(Troll):
    def __init__(self):
        self._health=50
        self._attack=10
        self._color='синий'
        
    def question(self):
        def prostoe(t):
            for i in range(2, t//2+1):
                if (t%i==0):
                    return 0
            return 1
        x=randint(1, 100)
        self.__quest=str(x)+ " - простое число? (формат ответа: 1/0)"
        self.set_answer(prostoe(x))
        return self.__quest

class RedTroll(Troll):
    def __init__(self):
        self._health=50
        self._attack=10
        self._color='красный'

    def question(self):
        def mnojitel(a):
            answer=[]
            t=2
            while t*t<=a:
                if a%t==0:
                    answer.append(t)
                    a//=t
                else:
                    t+=1
            if a>1:
                answer.append(a)
            return answer
        x=randint(1, 100)
        self.__quest="Разложи число " +str(x)+ " на множители и перечисли их через запятую в порядке возрастания (без 1)."
        ans=mnojitel(x)
        self.set_answer(ans)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon]
troll_types=[WhiteTroll, BlueTroll, RedTroll]
