import math


def calcBalance(balance, irate, prate, months):
    irate_monthly = irate/12
    min_pay = balance*prate
    balance -= min_pay
    balance += balance*irate_monthly
    if months == 1:
        return balance
    else:
        return calcBalance(balance, irate, prate, months-1)


def calcPayment(balance, irate, payment):
    for n in range(12):
        irate_monthly = irate/12
        balance -= payment
        balance += balance*irate_monthly
    return balance


balance = 320000
annualInterestRate = 0.2
min_payment = balance/12
max_payment = balance*pow((1+annualInterestRate), 12)/12
epsilon = 0.01
payment = (max_payment + min_payment)/2
while abs(calcPayment(balance, annualInterestRate, payment)) > epsilon:
    if calcPayment(balance, annualInterestRate, payment) > epsilon:
        min_payment = payment
    elif calcPayment(balance, annualInterestRate, payment) < epsilon:
        max_payment = payment
    payment = (max_payment + min_payment)/2
    print(payment)

print("Lowest payment: ", round(payment, 2))
