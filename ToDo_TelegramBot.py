import telebot
from random import choice

token = ' '  # Specify the Telegram bot "token".
bot = telebot.TeleBot(token)

helper = '''
/help - вывести справку по программе.
/add - добавить задачу в список (формат ввода: "/add 'дата' 'текст задачи'").
/show - вывести добавленные задачи.
/print - вывести добавленные задачи.
/random - добавить случайную задачу на дату "Сегодня".'''

ToDo_tasks = {}

random_task = ['Пройти курс по "SQL"', 'Прослушать лекцию по ООП',
               'Решить задачу на "Python"', 'Сходить в магазин за продуктами']


@bot.message_handler(commands=['help'])
def help_function(message):
    bot.send_message(message.chat.id, helper)


def add_ToDo(date, task):
    if date in ToDo_tasks:
        ToDo_tasks[date].append(task)
    else:
        ToDo_tasks[date] = []
        ToDo_tasks[date].append(task)


@bot.message_handler(commands=['add'])
def add_function(message):
    command = message.text.split(maxsplit=2)
    if len(command[2]) < 3:
        answer = 'Ошибка, описание задачи должно состоять не менее чем из трёх символов.'
        bot.send_message(message.chat.id, answer)
    else:
        date = command[1].lower()
        task = command[2]
        add_ToDo(date, task)
        answer = f'Задача {task} добавлена на дату {date}.'
        bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['random'])
def random_function(message):
    date = 'сегодня'
    task = choice(random_task)
    add_ToDo(date, task)
    answer = f'Задача {task} добавлена на дату {date}.'
    bot.send_message(message.chat.id, answer)


@bot.message_handler(commands=['show', 'print'])
def show_function(message):
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ''
    if date in ToDo_tasks:
        text = date.upper() + '\n'
        for task in ToDo_tasks[date]:
            text = text + '[] ' + task + '\n'
    else:
        text = 'Задач на эту дату нет.'
    bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
