# Let's create a bot that wants to get a job and demonstrates its abilities :)

def greet(bot_name, birth_year):  # greetings
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')


def remind_name():  # user's name
    print('Please, remind me your name.')
    name = input()
    print(f'What a great name you have, {name}!')


def guess_age():  # age test
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3, rem5, rem7 = (int(input()) for _ in range(3))
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}: that's a good time to review my resume and take me to the team :)")


def count():  # test of counting
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr += 1


def quiz():  # test of quiz
    print("Let's find out why you might consider my candidacy.")
    print('Please enter one number with a variant.')
    print()
    print('1. Our passion is to view resumes.')
    print('2. Because you are learning Python and have already learned something!')
    print('3. We accidentally entered this site. How to get out?')
    print('4. Because you have responded to our proposal.')

    answer = str(input())
    if answer == str(2) or answer == str(4):
        print("That's right, good luck to all of us! :)")
    else:
        while answer != str(2) or answer != str(4):
            if answer == str(1) or answer == str(3):
                print('Wrong answer, please try again.')
            elif answer == str(2) or answer == str(4):
                print("That's right, good luck to all of us! :)")
                break
            else:
                print('You have entered unsuitable characters. Please enter character 1, 2, 3 or 4. ')
            answer = str(input())


def end():  # tests are over
    print("Congratulations, have a nice day! Don't forget to contact me 😉")


greet('Pyid', '2021')
remind_name()
guess_age()
count()
print()
quiz()
end()
