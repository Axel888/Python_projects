from math import log, ceil  # импортируем из модуля "math" функции "log" и "ceil" (округление вверх)

print('What do you want to calculate?')  # что вы хотите рассчитать?
print('type "n" for number of monthly payments,')  # кол-во ежемесячных платежей
print('type "a" for annuity monthly payment amount,')  # размер аннуитетного ежемесячного платежа
print('type "p" for loan principal:')  # основная сумма кредита

calculate = input()


if calculate == 'n':  # кол-во ежемесячных платежей
    print('Enter the loan principal:')  # введите сумму кредита
    loan_principal = float(input())
    print('Enter the monthly payment:')  # введите ежемесячный платёж
    monthly_payment = float(input())
    print('Enter the loan interest:')  # введите проценты по кредиту
    loan_interest = float(input())
    i = loan_interest / (12 * 100) # номинальная процентная ставка
    x = monthly_payment / (monthly_payment - i * loan_principal)  # "x" для "log"
    base = 1 + i  # "base" для "log"
    periods = ceil(log(x, base))  # кол-во периодов (с округлением до полных месяцев)

    if periods == 1:  # условия по окончаниям (год / годЫ, месяц / месяцЫ) --> НУЖНО РЕВЬЮ
        answer = f'It will take 1 month to repay this loan!'
    elif periods == 0 or 1 < periods < 12:
        answer = f'It will take {periods} months to repay this loan!'
    elif periods == 12:
        answer = f'It will take 1 year to repay this loan!'
    elif periods % 12 == 0:
        answer = f'It will take {periods // 12} years to repay this loan!'
    else:
        if periods // 12 == 1 and periods % 12 != 0:
            answer = f'It will take 1 year and {periods % 12} months to repay this loan!'
        else:
            answer = f'It will take {periods // 12} years and {periods % 12} months to repay this loan!'


elif calculate == 'a':  # размер аннуитетного ежемесячного платежа
    print('Enter the loan principal:')  # введите сумму кредита
    loan_principal = float(input())
    print('Enter the number of periods:')  # введите кол-во периодов (месяцев)
    periods = float(input())
    print('Enter the loan interest:')  # введите проценты по кредиту
    loan_interest = float(input())
    i = loan_interest / (12 * 100) # номинальная процентная ставка
    monthly_payment = ceil(loan_principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods -1)))  # ежемесячный платёж
    answer = f'Your monthly payment = {monthly_payment}!'


elif calculate == 'p':  # основная сумма кредита
    print('Enter the annuity payment:')  # введите аннуитетный платеж
    annuity_payment = float(input())
    print('Enter the number of periods:')  # введите кол-во периодов (месяцев)
    periods = float(input())
    print('Enter the loan interest:')  # введите проценты по кредиту
    loan_interest = float(input())
    i = loan_interest / (12 * 100) # номинальная процентная ставка
    loan_principal = int(annuity_payment / (i * (1 +i ) ** periods / ((1 + i) ** periods - 1)))  # сумма кредита
    answer = f'Your loan principal = {loan_principal}!'


print(answer)  # вывод ответа
