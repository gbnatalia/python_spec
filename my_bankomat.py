import tkinter as tk
from dz2 import Bankomat


class MyBankomat(tk.Tk):

    def __init__(self):
        '''
        конструктор класса
        '''
        super().__init__()
        self.configure(width=50, height=120, bg='#721509')  # '#4c1e3c')
        self.title(r"Банкомат")
        self.bank = Bankomat()

        #########################################################################
        # Наименования операций
        name_operation = [
            "Пополнить счет",  # 1
            "Снять со счета",  # 2
            "Вывести информацию о счете",  # 3
            "Завершить работу",  # 4
        ]
        #######################################################################
        # Фрейм отображения баланса и сообщения оператору
        #
        display_balance_frame = tk.Frame(self)
        display_balance_frame.pack(side=tk.TOP, expand=0, fill='x', pady=10, padx=10)
        l_balance = tk.Label(display_balance_frame, text="Текущий баланс:", width=20)
        self.e_balance = tk.Entry(display_balance_frame, width=30)
        self.e_balance.configure(disabledbackground="white", disabledforeground="black")
        l_balance.pack(side=tk.LEFT, padx=5)
        self.e_balance.pack(side=tk.LEFT, padx=5)

        #######################################################################
        # Фрейм отображения сообщения оператору
        #
        display_msg_frame = tk.Frame(self, height=4, width=50, pady=10)
        display_msg_frame.pack(side=tk.TOP, expand=0, fill='x')
        l_msg = tk.Label(display_msg_frame, text="Информация:", width=15)
        l_msg.pack(side=tk.TOP, padx=5)
        self.memo = tk.Text(display_msg_frame, height=4, width=50)
        self.memo.pack(side=tk.TOP, padx=2)

        #######################################################################
        # Фрейм набора суммы
        #
        num_frame = tk.Frame(self)
        num_frame.pack(side=tk.TOP, expand=0, fill='x', pady=10, padx=10)
        l_amount = tk.Label(num_frame, text="Сумма пополнения/снятия (y.e):", width=30)
        self.sp_amount = tk.Spinbox(num_frame, width=10, from_=50.0,
                                    to=1000000000.0, increment=50)
        self.sp_amount.configure(disabledbackground="white", disabledforeground="black")
        l_amount.pack(side=tk.LEFT, padx=5)
        self.sp_amount.pack(side=tk.LEFT, padx=5)

        #######################################################################
        # Строка выбора действия        
        #
        todo_frame = tk.Frame(self).pack(side=tk.TOP, expand=0, fill='x')
        label = tk.Label(todo_frame, text="Выберите операцию:", fg="#721509",
                         font="Arial 16 bold")
        label.pack(fill='x', pady=10, padx=10)

        #######################################################################
        # Фрейм выбора операции
        #
        main_frame = tk.Frame(self).pack(side=tk.TOP, fill='x')

        btns_opt = {'bg': "#7a748c", 'fg': "#721509", 'font': "Arial 12 bold",
                    'justify': tk.LEFT}
        pack_opts = {'fill': 'x', 'side': tk.TOP, 'padx': 10, 'pady': 3, 'ipadx': 5}

        btns = list()
        for i in range(len(name_operation)):
            btns.append(tk.Button(main_frame, text=name_operation[i], **btns_opt))
            btns[i].pack(**pack_opts)
        btns[0]['command'] = lambda: self.__choose_op(0)
        btns[1]['command'] = lambda: self.__choose_op(1)
        btns[2]['command'] = lambda: self.__choose_op(2)
        btns[3]['command'] = lambda: self.__choose_op(3)

        msg = self.bank.get_history()
        balance = self.bank.get_balance()
        self.__show_data(balance, msg)

    def __show_data(self, balance, msg):
        '''
        Отображение информации о счете
        '''
        self.e_balance.delete(0, tk.END)
        self.e_balance.insert(0, f"{balance:.2f}")
        self.e_balance.update()
        self.memo.delete(1.0, tk.END)
        if len(msg):
            self.memo.insert(tk.END, msg)
        else:
            self.memo.insert(tk.END, "нет данных")
        self.memo.update()

    def __choose_op(self, num):
        '''
        Обработка нажатия кнопок
        '''
        # Добавление
        if num == 0:
            money = int(self.sp_amount.get())
            balance, msg = self.bank.add_money(money)
            self.__show_data(balance, msg)

        # Снятие
        elif num == 1:
            money = int(self.sp_amount.get())
            balance, msg = self.bank.withdraw_money(money)
            self.__show_data(balance, msg)

        # История операций
        elif num == 2:
            msg = self.bank.get_history()
            balance = self.bank.get_balance()
            self.__show_data(balance, msg)

        # выход
        else:
            app.quit()


if __name__ == "__main__":
    app = MyBankomat()
    app.mainloop()
