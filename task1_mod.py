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
        self.workers.append({'tel': t_num, 'sex': sex, 'otdel': o_num, 'last_name': last_name,
                             'oklad': okl, 'date': date, 'nadb': nadb, 'nds': nds, 'workin_days': workin_days,
                             'work_days': work_days, 'nach': nach, 'uder': uder})

    def delete_worker(self, ind_del):
        del self.workers[ind_del]

    def change_worker(self, ind_chg, t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder):
        self.workers[ind_chg] = {'tel': t_num, 'sex': sex, 'otdel': o_num, 'last_name': last_name,
                             'oklad': okl, 'date': date, 'nadb': nadb, 'nds': nds, 'workin_days': workin_days,
                             'work_days': work_days, 'nach': nach, 'uder': uder}

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
                        temp['tel'],
                        temp['sex'],
                        temp['otdel'],
                        temp['last_name'],
                        temp['oklad'],
                        temp['date'],
                        temp['nadb'],
                        temp['nds'],
                        temp['workin_days'],
                        temp['work_days'],
                        temp['nach'],
                        temp['uder'],
                    )

                )
                table.append(line)
            except:
                break

        return '\n'.join(table)

    def show_find(self):
        table = []
        itr = iter(self.find_table)
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
                        temp['tel'],
                        temp['sex'],
                        temp['otdel'],
                        temp['last_name'],
                        temp['oklad'],
                        temp['date'],
                        temp['nadb'],
                        temp['nds'],
                        temp['workin_days'],
                        temp['work_days'],
                        temp['nach'],
                        temp['uder'],
                    )

                )
                table.append(line)
            except:
                break

        return '\n'.join(table)

    def find_person_standart(self, key, znach):
        itr = iter(self.workers)
        self.find_table = []
        while True:
            try:
                temp = next(itr)
                if temp[key] == znach:
                    self.find_table.append(temp)
            except:
                break
        print(self.find_table)

    def save_as_txt(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self.show())
            f.close()
