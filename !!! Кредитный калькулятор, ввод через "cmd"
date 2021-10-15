import argparse  # Импортируем модуль "argparse".
from math import log, ceil  # Импортируем из модуля "math" функции "log" и "ceil" (округление вверх).

# Создаём переменную и применяем к ней модуль "argparse".
parser = argparse.ArgumentParser(
    description='''This program is a loan calculator. If you want to make a calculation, 
    then enter the type of payment, interest rate and any two parameters from the rest.''')
    # 'Эта программа - кредитный калькулятор. Если вы хотите произвести рассчёт,
    # то введите тип платежа, процентную ставку и любые два параметра из оставшихся.'

# Добавляем аргументы к нашей переменной.
parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    help="Please select the type of payment: 'annuity' "
                         "or 'diff' (annuity or differentiated).")
                    # 'Пожалуйста, выберите тип платежа: аннуететный или дифференцированный'.

parser.add_argument("--payment", type=float,
                    help="Please enter the monthly payment.")
                    # 'Пожалуйста, введите сумму ежемесячного платежа'.

parser.add_argument("--principal", type=float,
                    help="Please enter the loan principal.")
                    # 'Пожалуйста, введите основную сумму кредита'.

parser.add_argument("--periods", type=float,
                    help="Please enter the number of months.")
                    # 'Пожалуйста, введите количество месяцев'.

parser.add_argument("--interest", type=float,
                    help="Please enter the interest on the loan.")
                    # 'Пожалуйста, введите проценты по кредиту'.

# Читаем вводимые юзером данные из командной строки
# с помощью метода ".parse_args()", применённому к нашей основной переменной.
args = parser.parse_args()


# Условия для определения размера ежемесячного аннуитетного платежа.
if args.type == 'annuity' and args.principal is not None \
        and args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Номинальная процентная ставка.
    payment = ceil(args.principal * ((i * (1 + i) ** args.periods)
                                     / ((1 + i) ** args.periods - 1)))  # Ежемесячный платёж.
    print(f'Your annuity payment = {payment}!')  # Ответ
    print(f'Overpayment = {ceil(payment * args.periods - args.principal)}')  # Переплата.

# Условия для определения периода аннуитетных платежей.
elif args.type == 'annuity' and args.principal is not None \
        and args.payment is not None and args.interest is not None:
    i = args.interest / (12 * 100) # Номинальная процентная ставка.
    x = args.payment / (args.payment - i * args.principal)  # "x" для "log".
    base = 1 + i  # "base" для "log".
    periods = ceil(log(x, base))  # Кол-во периодов (с округлением до полных месяцев).
    if periods == 1:  # Условия по окончаниям (год / годЫ, месяц / месяцЫ) --> НУЖНО РЕВЬЮ.
        print(f'It will take 1 month to repay this loan!')
    elif periods == 0 or 1 < periods < 12:
        print(f'It will take {periods} months to repay this loan!')
    elif periods == 12:
        print(f'It will take 1 year to repay this loan!')
    elif periods % 12 == 0:
        print(f'It will take {periods // 12} years to repay this loan!')
    else:
        if periods // 12 == 1 and periods % 12 != 0:
            print(f'It will take 1 year and {periods % 12} months to repay this loan!')
        else:
            print(f'It will take {periods // 12} years and {periods % 12} months to repay this loan!')
    print(f'Overpayment = {ceil(args.payment * periods - args.principal)}')  # Переплата.

# Условия для определения основной суммы займа, при аннуитетных платежах.
elif args.type == 'annuity' and args.payment is not None \
        and args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Номинальная процентная ставка.
    principal = int(args.payment / (i * (1 +i ) ** args.periods
                                    / ((1 + i) ** args.periods - 1)))  # Сумма займа.
    print(f'Your loan principal = {principal}!')  # Ответ.
    print(f'Overpayment = {ceil(args.payment * args.periods - principal)}')  # Переплата.

# Условия для определения ежемесячных дифференцированных платежей.
elif args.type == 'diff' and args.principal is not None and \
        args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Номинальная процентная ставка.
    total_payment = 0
    for m in range(1, int(args.periods) + 1):
        payment = args.principal / args.periods + \
                  i * (args.principal - (args.principal * (m - 1) / args.periods))
        total_payment += ceil(payment)
        print(f'Month {m}: payment is {ceil(payment)}')  # Ежемесячные платежи.
    print(f'Overpayment = {ceil(total_payment - args.principal)}')  # Переплата.

else:  # Если ввод не соответствует условиям.
    print('Incorrect parameters')  # 'Параметры неверны'.
