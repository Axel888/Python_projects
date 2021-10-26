# Устанавливаем библиотеку с готовыми скриптами по созданию Телеграм-бота:
# в терминале вводим "pip3 install --user pytelegrambotapi".

import telebot  # Импортируем модуль для работы с Телеграм-ботом.
from random import choice

token = ' '  # Указать "токен" Телеграм-бота.
bot = telebot.TeleBot(token)  # Создаем КЛЮЧЕВУЮ для всей программы переменную bot.

# Список команд. Для Телеграм-бота команда начинается со знака "/".
helper = '''
/help - вывести справку по программе.
/add - добавить задачу в список (формат ввода: "/add 'дата' 'текст задачи'").
/show - вывести добавленные задачи.
/print - вывести добавленные задачи.
/random - добавить случайную задачу на дату "Сегодня".'''

# Вводим словарь, в который будут добавляться задачи.
ToDo_tasks = {}

# Список случайных задач.
random_task = ['Пройти курс по "SQL"', 'Прослушать лекцию по ООП',
               'Решить задачу на "Python"', 'Сходить в магазин за продуктами']

# Метод "message_handler" - обработчик команд от пользователя.
@bot.message_handler(commands=['help'])
def help_function(message):
    bot.send_message(message.chat.id, helper)

def add_ToDo(date, task):   # Распределяет задачи в словаре "ToDo_tasks" по дате.
    if date in ToDo_tasks:
        ToDo_tasks[date].append(task)
    else:
        ToDo_tasks[date] = []
        ToDo_tasks[date].append(task)

@bot.message_handler(commands=['add'])
def add_function(message):
    command = message.text.split(maxsplit=2)
    if len(command[2]) < 3:
        # Ответ пользователю (переменнная "answer").
        answer = 'Ошибка, описание задачи должно состоять не менее чем из трёх символов.'
        bot.send_message(message.chat.id, answer)  # Сообщение для пользователя от бота.
    else:
        date = command[1].lower()  # Чтобы ввод по датам не делился по разному регистру.
        task = command[2]
        add_ToDo(date, task)
        answer = f'Задача {task} добавлена на дату {date}.'
        bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['random'])
def random_function(message):
    date = 'сегодня'  # Добавляем случайную задачу на эту дату.
    task = choice(random_task)  # Делаем случайный выбор задачи из списка "random_task".
    add_ToDo(date, task)
    answer = f'Задача {task} добавлена на дату {date}.'
    bot.send_message(message.chat.id, answer)

@bot.message_handler(commands=['show', 'print'])
def show_function(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()  # Чтобы вывод по датам не делился по разному регистру.
    text = ''  # Вводим переменную, отображающую задачи.
    if date in ToDo_tasks:
        text = date.upper() + '\n'
        for task in ToDo_tasks[date]:
            # В переменную "text" добавляем все задачи, которые есть на введённую дату.
            text = text + '[] ' + task + '\n'
    else:
        text = 'Задач на эту дату нет.'
    bot.send_message(message.chat.id, text)

bot.polling(none_stop=True)  # Постоянно отправляет запросы серверам "Telegram".



