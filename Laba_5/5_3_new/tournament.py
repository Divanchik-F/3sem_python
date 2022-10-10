 # coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = list(map(int, input(message).split(',')))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, monster_list):
    for monster in monster_list:
        print('Вышел', monster._color, 'дракон!')
        while monster.is_alive() and hero.is_alive():
            print('Вопрос:', monster.question())
            answer = annoying_input_int('Ответ:')

            if monster.check_answer(answer):
                hero.attack(monster)
                print('Верно! \n** дракон кричит от боли **')
            else:
                monster.attack(hero)
                print('Ошибка! \n** вам нанесён удар... **')
        if monster.is_alive():
            break
        print('Дракон', monster._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        monster_number = 6
        monster_list = generate_enemy_list(monster_number)
        assert(len(monster_list) == 6)
        print('У Вас на пути', monster_number, 'монстров!')
        game_tournament(hero, monster_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
