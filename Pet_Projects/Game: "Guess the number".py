from random import *


def is_valid(num):  # Checking the entered number for correctness.
    while True:
        if num.isdigit() == True and 1 <= int(num) <= 10:
            return int(num)
        else:
            num = input('А может быть все-таки введем целое число от 1 до 10? \n')
            continue


def game():  # Program.
    while True:
        print('Добро пожаловать в числовую угадайку!')
        hidden_num = randint(1, 10)
        counter = 0

        # Checking the number entered by the user.
        answer = is_valid(input('Введите целое число от 1 до 10 включительно \n'))

        while True:  # Tests for equality and counting attempts to guess.
            if answer < hidden_num:
                answer = is_valid(input('Ваше число меньше загаданного, попробуйте еще разок \n'))
                counter += 1
                continue
            elif answer > hidden_num:
                answer = is_valid(input('Ваше число больше загаданного, попробуйте еще разок \n'))
                counter += 1
                continue
            else:
                counter += 1
                print('Вы угадали!')
                print(f'Количество попыток, которое потребовалось для этого: {counter}.')
                print('Поздравляем!')
                break
        break


while True:  # Start.
    print('Хотите сыграть в игру, отгадать загаданное число от 1 до 10? (Да / Нет)')
    if input().lower() == 'да':
        game()
    else:
        print('Спасибо, что уделили внимание! Еще увидимся!')
        break
