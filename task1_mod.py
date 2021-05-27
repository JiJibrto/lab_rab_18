# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Реализовать класс, используя в качестве контейнера список Python. С контейнером
# выполняются операции добавления в конец контейнера, удаления и замены элемента
# контейнера. Использовать методы контейнера. Реализовать перебор элементов с помощью
# итераторов. Основной операцией является операция поиска и выборки подмножества
# контейнера по заданным критериям. Операцию поиска реализовать в двух вариантах:
# использовать алгоритмы последовательного поиска;
# сортировать исходный контейнер и использовать алгоритмы двоичного поиска.
# При поиске осуществлять сохранение выбранных записей в другой список. Написать функцию,
# осуществляющую вывод очереди в текстовый файл в виде ведомости с подведением общих
# итогов.

# Сотрудник представлен структурой Person с полями; табельный номер, номер отдела,
# фамилия, оклад, дата поступления на работу, процент надбавки, подоходный налог,
# количество отработанных дней в месяце, количество рабочих дней в месяце, начислено,
# удержано. Поиск по номеру отдела, полу, дате поступления, фамилии

class Staff():
    def __init__(self):
        self.workers = []
        self.find_table = []

    def add(self, t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder):
        self.workers.append([t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder])

    def delete_worker(self, ind_del):
        del self.workers[ind_del]

    def change_worker(self, ind_chg, t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder):
        self.workers[ind_chg] = [t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder]

    def show(self):
        table = []
        itr = iter(self.workers)
        line = "+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+".format(
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5,
            '-' * 5
        )
        table.append(line)
        table.append((
            "| {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} |".format(
                "t_num",
                "sex",
                "o_num",
                "l_n",
                "okl",
                "date",
                "nadb",
                "nds",
                "win_d",
                "wk_d",
                "nach",
                "uder"
            )
        )
        )
        table.append(line)
        while True:
            try:
                temp = next(itr)
                print(temp)
                table.append(
                    "| {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} |".format(
                        temp[0],
                        temp[1],
                        temp[2],
                        temp[3],
                        temp[4],
                        temp[5],
                        temp[6],
                        temp[7],
                        temp[8],
                        temp[9],
                        temp[10],
                        temp[11],
                    )

                )
                table.append(line)
            except:
                break

        return '\n'.join(table)

    def find_person_standart(self, column, znach):
        itr = iter(self.workers)
        self.find_table = []
        while True:
            try:
                temp = next(itr)
                if temp[column] == znach:
                    self.find_table.append(temp[column])
            except:
                break