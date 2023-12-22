# У вас есть банковская карта с начальным балансом равным 0 у.е. 
# Вы хотите управлять этой картой, выполняя следующие операции, 
# для выполнения которых необходимо написать следующие функции:
# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []

removal = decimal.Decimal(0)

def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        return False

def deposit(amount):
    global bank_account, count, operations
    if check_multiplicity(amount):
        bank_account = decimal.Decimal(bank_account + amount)
        operations.append(f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е.")
        count += 1
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        
def withdraw(amount):
    global bank_account, count, operations 
    
    for i in range(int(MIN_REMOVAL),int(MAX_REMOVAL)):
        if i < amount:
            if amount > MAX_REMOVAL:
                removal = 45
            else:
                removal = decimal.Decimal(i)
            break
        
    if check_multiplicity(amount):
        if amount > bank_account:
            operations.append(f'Недостаточно средств. Сумма с комиссией {decimal.Decimal(amount + removal)} у.е. На карте {bank_account} у.е.')
        else:
            bank_account = decimal.Decimal(bank_account - amount - decimal.Decimal(removal))
            operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {removal} у.е.. Итого {bank_account} у.е.')
    else:
        operations.append(f'Недостаточно средств. Сумма с комиссией 51 у.е. На карте {bank_account} у.е.')
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        
def exit():
    global bank_account, operations
    procent = 0.000
    if bank_account > RICHNESS_SUM:
        procent = decimal.Decimal(bank_account * RICHNESS_PERCENT)
        bank_account = bank_account - procent
        operations.append(f'Вычтен налог на богатство 0.1% в сумме {round(procent,4)} у.е. Итого {round(bank_account,4)} у.е.')
        operations.append(f'Возьмите карту на которой {round(bank_account,4)} у.е.')
    
    else:
        operations.append(f'Возьмите карту на которой {round(bank_account)} у.е.')


    
   
deposit(1000000000000000)
withdraw(200)
withdraw(300)
deposit(500)
withdraw(3000)
exit()

print(operations)
