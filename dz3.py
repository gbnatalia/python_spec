'''
Напишите программу банкомат.
Начальная сумма равна нулю.
 Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
✔ Дополнительно сохраняйте все операции поступления и снятия средств в список.
Разбейте её на отдельные операции — функции.
'''

def add_money(balance):
    if balance >= 5000000:
        balance = balance * 0.9
    amount = int(input("Введите сумму для пополнения (кратную 50): "))
    while amount % 50 != 0:
        amount = int(input("Сумма должна быть кратна 50, введите сумму ещё раз: "))
    balance += amount
    print(f"На вашем балансе {balance} у.е.")
    return balance, amount

def withdraw_money(balance):
    if balance >= 5000000:
        balance = balance * 0.9

    amount = int(input("Введите сумму для снятия (кратную 50): "))
    while amount % 50 != 0 or amount > balance:
        if amount % 50 != 0:
            amount = int(input("Сумма должна быть кратна 50, введите сумму ещё раз: "))
        else:
            amount = int(input("На вашем счете недостаточно средств для снятия, введите сумму ещё раз: "))

    if amount >= 10000:
        commission = max(amount * 0.015, 30)
        balance -= (amount + commission)
        print(f"Вы сняли {amount} у.е., комиссия составила {commission} у.е.")
    else:
        balance -= amount
        print(f"Вы сняли {amount} у.е.")

    print(f"На вашем балансе {balance} у.е.")

    return balance, amount

def bankomat():

    balance = 0
    operations = []

    while True:

        print("Выберите действие:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "3":
            print("До свидания!")
            print(f"На вашем счете осталось {balance} у.е.")
            for op in operations:
                print(op)
            break
            
        else:

            if choice == "1":
                balance, amount = add_money(balance)
                operations.append(f"Пополнение: +{amount} у.е.")
            else:   # choice == "2"
                balance, amount = withdraw_money(balance)
                operations.append(f"Снятие: -{amount} у.е.")

            if len(operations) % 3 == 0:
                balance += balance * 0.03

if __name__=="__main__":
    bankomat()