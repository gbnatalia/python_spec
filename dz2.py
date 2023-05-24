'''
Возьмите задачу из прошлых семинаров, которые вы уже решали. 
Превратите функции в методы класса, а параметры в свойства. 
Задачи должны решаться через вызов методов экземпляра. 

Напишите программу банкомат.
Начальная сумма равна нулю.
 Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
на сумму 
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 50 млн, вычитать налог на богатство 10%
  перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
✔ Дополнительно сохраняйте все операции поступления и снятия средств в список.
'''


class Bankomat:
    __cnt_operation = 0
    __history = []

    def __init__(self):
        self.__balance = 0

    def __get_nalog(self):
        msg = ""
        if self.__balance >= 5000000:
            self.__balance = self.__balance * 0.9
            msg = f"Налог на богатство-10%. Тек.баланс-{self.__balance:.2f} y.e. "
            self.__history.append(msg)
        return msg + "\n"

    def __add_procent(self, msg):
        full_msg = msg
        self.__cnt_operation = self.__cnt_operation + 1
        self.__history.append(msg)
        if self.__cnt_operation % 3 == 0:
            self.__balance = self.__balance * 1.03
            msg = f"Начисление 3% процентов. Тек.баланс-{self.__balance:.2f} y.e."
            self.__history.append(msg)
            full_msg += "\n" + msg
        return full_msg

    def add_money(self, amount):
        '''
        пополнение счета
        :param amount: сумма, вносимая в банкомат (д.б.кратна 50)
        :return: текущее значение баланса, сообщение потребителю        
        '''
        full_msg = self.__get_nalog()
        if amount % 50 != 0:
            full_msg += "Сумма для пополнения должна быть кратна 50!"
        else:
            self.__balance += amount
            msg = f"Пополнение на {amount} y.e. "
            full_msg += self.__add_procent(msg)
        return self.__balance, full_msg

    def withdraw_money(self, amount):
        '''
        снятие со счета
        :param amount: снимаемая сумма (д.б.кратна 50)
        :return: текущее значение баланса, сообщение потребителю        
        '''
        full_msg = self.__get_nalog()
        if amount % 50 != 0:
            full_msg += "Сумма для снятия должна быть кратна 50!"
        elif self.__balance - amount < 0:
            full_msg += "На вашем счете недостаточно средств для снятия"
        else:
            if amount >= 10000:
                commission = max(amount * 0.015, 30)
                self.__balance -= (amount + commission)
                msg = f"Снятие {amount} у.е. Комиссия-{commission} у.е. "
            else:
                self.__balance -= amount
                msg = f"Снятие {amount} y.e. "
            full_msg += self.__add_procent(msg)

        return self.__balance, full_msg

    def get_history(self):
        '''
        получение истории операций
        '''
        history = ""
        for op in self.__history:
            history += f"{op}\n"
        return history

    def get_balance(self):
        '''
        получение текущего баланса
        '''
        return self.__balance


if __name__ == "__main__":

    def test_bankomat():

        bank = Bankomat()

        while True:

            print("\nВыберите действие:")
            print("1. Пополнить")
            print("2. Снять")
            print("3. Выйти")

            try:
                choice = input("\nВведите номер действия: ")

                if choice == "3":
                    print("\nДо свидания!")
                    print(f"На вашем счете осталось {bank.get_balance()} у.е.")
                    print("История операций:")
                    print(bank.get_history())
                    break
                elif choice == "1":
                    amount = int(input("Введите сумму для внесения: "))
                    balance, msg = bank.add_money(amount)
                    print("")
                    print(msg)
                    print(f"Текущий баланс - {balance}")
                elif choice == "2":
                    amount = int(input("Введите сумму для снятия: "))
                    balance, msg = bank.withdraw_money(amount)
                    print("")
                    print(msg)
                    print(f"Текущий баланс - {balance}")
                else:
                    print("\nВведено неизвестное действие!")
            except:
                print("\nВы испортили банкомат. Все ваши средства сгорели!")
                break


    test_bankomat()
