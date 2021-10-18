from random import *

# Генератор паролей.
def generate_password(length, set):
    password = sample(set, length)
    password = ''.join(password)
    return password

# Необходимые переменные.
digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
exclude = 'il1Lo0O'
chars = ''

# Приветствие и вопросы пользователю.
print('Данная программа создана для генерации безопасных паролей. \n')
question_1 = int(input('Укажите количество паролей для генерации: \n'))
question_2 = int(input('Укажите длину одного пароля: \n'))
question_3 = input('Должны ли пароли включать цифры: "0123456789" ? (Да / Нет) \n')
question_4 = input('Должны ли пароли включать прописные буквы: "ABCDEFGHIJKLMNOPQRSTUVWXYZ" ? (Да / Нет) \n')
question_5 = input('Должны ли пароли включать строчные буквы: "abcdefghijklmnopqrstuvwxyz" ? (Да / Нет) \n')
question_6 = input('Должны ли пароли включать символы: "!#$%&*+-=?@^_" ? (Да / Нет) \n')
question_7 = input('Должны ли пароли исключать неоднозначные символы: "il1Lo0O" ? (Да / Нет) \n')


# Алгоритм программы.
if question_3.lower() == 'да':
    chars += digits
if question_4.lower() == 'да':
    chars += uppercase_letters
if question_5.lower() == 'да':
    chars += lowercase_letters
if question_6.lower() == 'да':
    chars += punctuation
if question_7.lower() != 'да':
    chars += exclude

# Вывод паролей.
for i in range(question_1):
    print(generate_password(question_2, chars))

