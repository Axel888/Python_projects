import argparse
from math import log, ceil

# Greetings and questions to the user.
parser = argparse.ArgumentParser(
    description='''This program is a loan calculator. If you want to make a calculation, 
    then enter the type of payment, interest rate and any two parameters from the rest.''')

parser.add_argument("--type",
                    choices=["annuity", "diff"],
                    help="Please select the type of payment: 'annuity' "
                         "or 'diff' (annuity or differentiated).")

parser.add_argument("--payment", type=float,
                    help="Please enter the monthly payment.")

parser.add_argument("--principal", type=float,
                    help="Please enter the loan principal.")

parser.add_argument("--periods", type=float,
                    help="Please enter the number of months.")

parser.add_argument("--interest", type=float,
                    help="Please enter the interest on the loan.")

# Reading the entered data.
args = parser.parse_args()

# Conditions for determining the amount of the monthly annuity payment.
if args.type == 'annuity' and args.principal is not None \
        and args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Nominal interest rate.
    payment = ceil(args.principal * ((i * (1 + i) ** args.periods)
                                     / ((1 + i) ** args.periods - 1)))  # Monthly payment.
    print(f'Your annuity payment = {payment}!')  # Answer.
    print(f'Overpayment = {ceil(payment * args.periods - args.principal)}')  # Overpayment.

# Conditions for determining the period of annuity payments.
elif args.type == 'annuity' and args.principal is not None \
        and args.payment is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Nominal interest rate.
    x = args.payment / (args.payment - i * args.principal)  # "x" for "log".
    base = 1 + i  # "base" for "log".
    periods = ceil(log(x, base))  # Number of periods (rounded to full months).
    if periods == 1:
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
    print(f'Overpayment = {ceil(args.payment * periods - args.principal)}')  # Overpayment.

# Conditions for determining the principal amount of the loan for annuity payments.
elif args.type == 'annuity' and args.payment is not None \
        and args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Nominal interest rate.
    principal = int(args.payment / (i * (1 + i) ** args.periods
                                    / ((1 + i) ** args.periods - 1)))  # Loan amount.
    print(f'Your loan principal = {principal}!')  # Answer.
    print(f'Overpayment = {ceil(args.payment * args.periods - principal)}')  # Overpayment.

# Conditions for determining monthly differentiated payments.
elif args.type == 'diff' and args.principal is not None and \
        args.periods is not None and args.interest is not None:
    i = args.interest / (12 * 100)  # Nominal interest rate.
    total_payment = 0
    for m in range(1, int(args.periods) + 1):
        payment = args.principal / args.periods + \
                  i * (args.principal - (args.principal * (m - 1) / args.periods))
        total_payment += ceil(payment)
        print(f'Month {m}: payment is {ceil(payment)}')  # Monthly payments.
    print(f'Overpayment = {ceil(total_payment - args.principal)}')  # Overpayment.

else:
    print('Incorrect parameters')
