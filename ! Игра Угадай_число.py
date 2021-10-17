from random import *


def is_valid(num):  # Проверка введённого числа на корректность.
    while True:
        if num.isdigit() == True and 1 <= int(num) <= 10:
            return int(num)
        else:
            num = input('А может быть все-таки введем целое число от 1 до 10? ')
            continue


def game():  # Алгоритм игры.
    while True:
        print('Добро пожаловать в числовую угадайку!')
        hidden_num = randint(1, 10)
        counter = 0

        # Проверяем введённое пользователем число.
        answer = is_valid(input('Введите целое число от 1 до 10 включительно: '))

        while True:  # Проверки на равенство и подсчёт попыток угадать.
            if answer < hidden_num:
                answer = is_valid(input('Ваше число меньше загаданного, попробуйте еще разок: '))
                counter += 1
                continue
            elif answer > hidden_num:
                answer = is_valid(input('Ваше число больше загаданного, попробуйте еще разок: '))
                counter += 1
                continue
            else:
                counter += 1
                print(f'''
Вы угадали! 
Количество попыток, которое потребовалось для этого: {counter}. 
Поздравляем!''')
                break
        break


while True:  # Начало игры.
    print('Хотите сыграть в игру, отгадать загаданное число от 1 до 10? (Да / Нет): ')
    if input().lower() == 'да':
        game()
    else:
        print('Спасибо, что уделили внимание! Еще увидимся!')
        break
