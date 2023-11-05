from math import log, ceil

print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')

calculate = input()

if calculate == 'n':  # Number of monthly payments.
    print('Enter the loan principal:')
    loan_principal = float(input())
    print('Enter the monthly payment:')
    monthly_payment = float(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / (12 * 100)  # Nominal interest rate.
    x = monthly_payment / (monthly_payment - i * loan_principal)  # "x" for "log".
    base = 1 + i  # "base" for "log".
    periods = ceil(log(x, base))

    if periods == 1:
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


elif calculate == 'a':  # Amount of the annuity monthly payment.
    print('Enter the loan principal:')
    loan_principal = float(input())
    print('Enter the number of periods:')
    periods = float(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / (12 * 100)  # Nominal interest rate.
    monthly_payment = ceil(loan_principal * ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    answer = f'Your monthly payment = {monthly_payment}!'


elif calculate == 'p':  # Principal amount of the loan.
    print('Enter the annuity payment:')
    annuity_payment = float(input())
    print('Enter the number of periods:')
    periods = float(input())
    print('Enter the loan interest:')
    loan_interest = float(input())
    i = loan_interest / (12 * 100)  # Nominal interest rate.
    loan_principal = int(annuity_payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1)))
    answer = f'Your loan principal = {loan_principal}!'

print(answer)
