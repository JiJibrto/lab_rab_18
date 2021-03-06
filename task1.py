# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import task1_mod as mod

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


def find_wind():
    def find_worker():
        staff.find_person_standart(var.get(), ent.get())
        mb.showinfo('', 'Успешно')
        show_find()
        find_window.destroy()

    find_window = Toplevel()

    find_window.resizable(False, False)
    var = StringVar()

    lab_1 = LabelFrame(find_window, text='Критерий поиска')
    lab_2 = LabelFrame(find_window, text='Значение')
    rad_1 = Radiobutton(lab_1, text="Номер отдела", indicatoron=0,
                        width=15, height=1,
                        variable=var, value="otdel")
    rad_2 = Radiobutton(lab_1, text="Пол", indicatoron=0,
                        width=15, height=1,
                        variable=var, value="sex")
    rad_3 = Radiobutton(lab_1, text="Дата поступления", indicatoron=0,
                        width=15, height=1,
                        variable=var, value="date")
    rad_4 = Radiobutton(lab_1, text="Фамилия", indicatoron=0,
                        width=15, height=1,
                        variable=var, value="last_name")
    ent = Entry(lab_2)
    but = Button(find_window, text='поиск', command=find_worker)

    lab_1.pack(side=LEFT)
    rad_1.pack(side=TOP)
    rad_2.pack(side=TOP)
    rad_3.pack(side=TOP)
    rad_4.pack(side=TOP)
    lab_2.pack(side=LEFT)
    but.pack(side=LEFT)
    ent.pack(side=LEFT)


def save_table():
    try:
        file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("All files", "*.*")))
        staff.save_as_txt(file_name)
        mb.showinfo('Файл сохранен', 'Успешно')
    except:
        mb.showinfo("Ошибка",
                    "Файл не выбран!")


def add_wind():
    # t_num, sex, o_num,
    # last_name, okl, date,
    # nadb, nds, workin_days,
    # work_days, nach, uder
    def add_work():
        t_num = str(ent_1.get())
        sex = str(ent_2.get())
        o_num = str(ent_3.get())
        last_name = str(ent_4.get())
        okl = str(ent_5.get())
        date = str(ent_6.get())
        nadb = str(ent_7.get())
        nds = str(ent_8.get())
        workin_days = str(ent_9.get())
        work_days = str(ent_10.get())
        nach = str(ent_11.get())
        uder = str(ent_12.get())
        staff.add(t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder)
        added_window.destroy()
        mb.showinfo('Успешно', 'Сотрудник добавлен в список')
        show()

    added_window = Toplevel()
    added_window.title('Добавить человека')
    added_window.resizable(False, False)
    main_lab_1 = Label(added_window)
    main_lab_2 = Label(added_window)
    lab_1_1 = LabelFrame(main_lab_1, text='Табельный номер')
    lab_2_1 = LabelFrame(main_lab_1, text='Пол')
    lab_3_1 = LabelFrame(main_lab_1, text='Номер отдела')
    lab_4_1 = LabelFrame(main_lab_1, text='Фамилия')
    lab_5_1 = LabelFrame(main_lab_1, text='Оклад')
    lab_6_1 = LabelFrame(main_lab_1, text='Дата поступления на работу')

    lab_1_2 = LabelFrame(main_lab_2, text='Надбавка')
    lab_2_2 = LabelFrame(main_lab_2, text='Подоходный налог')
    lab_3_2 = LabelFrame(main_lab_2, text='Кол-во отработанных дней')
    lab_4_2 = LabelFrame(main_lab_2, text='Кол-во рабочих смен')
    lab_5_2 = LabelFrame(main_lab_2, text='Начислено')
    lab_6_2 = LabelFrame(main_lab_2, text='Удержано')

    ent_1 = Entry(lab_1_1)
    ent_2 = Entry(lab_2_1)
    ent_3 = Entry(lab_3_1)
    ent_4 = Entry(lab_4_1)
    ent_5 = Entry(lab_5_1)
    ent_6 = Entry(lab_6_1)
    ent_7 = Entry(lab_1_2)
    ent_8 = Entry(lab_2_2)
    ent_9 = Entry(lab_3_2)
    ent_10 = Entry(lab_4_2)
    ent_11 = Entry(lab_5_2)
    ent_12 = Entry(lab_6_2)
    btn_1 = Button(added_window, text='Добавить', command=add_work)

    main_lab_1.pack(side=TOP)
    main_lab_2.pack(side=TOP)
    lab_1_1.pack(side=LEFT)
    lab_2_1.pack(side=LEFT)
    lab_3_1.pack(side=LEFT)
    lab_4_1.pack(side=LEFT)
    lab_5_1.pack(side=LEFT)
    lab_6_1.pack(side=LEFT)
    lab_1_2.pack(side=LEFT)
    lab_2_2.pack(side=LEFT)
    lab_3_2.pack(side=LEFT)
    lab_4_2.pack(side=LEFT)
    lab_5_2.pack(side=LEFT)
    lab_6_2.pack(side=LEFT)

    ent_1.pack(side=LEFT)
    ent_2.pack(side=LEFT)
    ent_3.pack(side=LEFT)
    ent_4.pack(side=LEFT)
    ent_5.pack(side=LEFT)
    ent_6.pack(side=LEFT)
    ent_7.pack(side=LEFT)
    ent_8.pack(side=LEFT)
    ent_9.pack(side=LEFT)
    ent_10.pack(side=LEFT)
    ent_11.pack(side=LEFT)
    ent_12.pack(side=LEFT)
    btn_1.pack(side=LEFT)


def change_wind_1():
    def change_mid():
        temp = int(ent_1.get()) - 1
        change_wind_2(temp)
        change_window_1.destroy()

    def change_wind_2(temp):
        def add_work(lol):
            t_num = str(ent_1.get())
            sex = str(ent_2.get())
            o_num = str(ent_3.get())
            last_name = str(ent_4.get())
            okl = str(ent_5.get())
            date = str(ent_6.get())
            nadb = str(ent_7.get())
            nds = str(ent_8.get())
            workin_days = str(ent_9.get())
            work_days = str(ent_10.get())
            nach = str(ent_11.get())
            uder = str(ent_12.get())
            staff.change_worker(temp, t_num, sex, o_num, last_name, okl, date, nadb, nds, workin_days, work_days, nach, uder)
            added_window.destroy()
            mb.showinfo('Успешно', 'Строка изменена')
            show()

        added_window = Toplevel()
        added_window.title('Добавить человека')
        added_window.resizable(False, False)
        main_lab_1 = Label(added_window)
        main_lab_2 = Label(added_window)
        lab_1_1 = LabelFrame(main_lab_1, text='Табельный номер')
        lab_2_1 = LabelFrame(main_lab_1, text='Пол')
        lab_3_1 = LabelFrame(main_lab_1, text='Номер отдела')
        lab_4_1 = LabelFrame(main_lab_1, text='Фамилия')
        lab_5_1 = LabelFrame(main_lab_1, text='Оклад')
        lab_6_1 = LabelFrame(main_lab_1, text='Дата поступления на работу')

        lab_1_2 = LabelFrame(main_lab_2, text='Надбавка')
        lab_2_2 = LabelFrame(main_lab_2, text='Подоходный налог')
        lab_3_2 = LabelFrame(main_lab_2, text='Кол-во отработанных дней')
        lab_4_2 = LabelFrame(main_lab_2, text='Кол-во рабочих смен')
        lab_5_2 = LabelFrame(main_lab_2, text='Начислено')
        lab_6_2 = LabelFrame(main_lab_2, text='Удержано')

        ent_1 = Entry(lab_1_1)
        ent_2 = Entry(lab_2_1)
        ent_3 = Entry(lab_3_1)
        ent_4 = Entry(lab_4_1)
        ent_5 = Entry(lab_5_1)
        ent_6 = Entry(lab_6_1)
        ent_7 = Entry(lab_1_2)
        ent_8 = Entry(lab_2_2)
        ent_9 = Entry(lab_3_2)
        ent_10 = Entry(lab_4_2)
        ent_11 = Entry(lab_5_2)
        ent_12 = Entry(lab_6_2)
        btn_1 = Button(added_window, text='Изменить')
        btn_1.bind('<Button-1>', add_work)

        main_lab_1.pack(side=TOP)
        main_lab_2.pack(side=TOP)
        lab_1_1.pack(side=LEFT)
        lab_2_1.pack(side=LEFT)
        lab_3_1.pack(side=LEFT)
        lab_4_1.pack(side=LEFT)
        lab_5_1.pack(side=LEFT)
        lab_6_1.pack(side=LEFT)
        lab_1_2.pack(side=LEFT)
        lab_2_2.pack(side=LEFT)
        lab_3_2.pack(side=LEFT)
        lab_4_2.pack(side=LEFT)
        lab_5_2.pack(side=LEFT)
        lab_6_2.pack(side=LEFT)

        ent_1.pack(side=LEFT)
        ent_2.pack(side=LEFT)
        ent_3.pack(side=LEFT)
        ent_4.pack(side=LEFT)
        ent_5.pack(side=LEFT)
        ent_6.pack(side=LEFT)
        ent_7.pack(side=LEFT)
        ent_8.pack(side=LEFT)
        ent_9.pack(side=LEFT)
        ent_10.pack(side=LEFT)
        ent_11.pack(side=LEFT)
        ent_12.pack(side=LEFT)
        btn_1.pack(side=LEFT)

    change_window_1 = Toplevel()
    lb_1 = LabelFrame(change_window_1, text='Введите номер строки которую собираетесь изменить')
    ent_1 = Entry(lb_1)
    btn_1 = Button(change_window_1, text='Изменить', command=change_mid)

    lb_1.pack()
    ent_1.pack()
    btn_1.pack()


def del_wind():
    def dele():
        temp = int(ent_1.get()) - 1
        staff.delete_worker(temp)
        show()
        delete_wind.destroy()
        mb.showinfo('Успешно', 'Строка удалена')
        show()

    delete_wind = Toplevel()
    lb_1 = LabelFrame(delete_wind, text='Введите номер строки которую собираетесь удалить')
    ent_1 = Entry(lb_1)
    btn_1 = Button(delete_wind, text='Удалить', command=dele)

    lb_1.pack()
    ent_1.pack()
    btn_1.pack()


def show():
    text.delete(0.0, END)
    text.insert(0.0, staff.show())


def show_find():
    text.delete(0.0, END)
    text.insert(0.0, staff.show_find())


if __name__ == '__main__':
    staff = mod.Staff()
    root = Tk()
    root.geometry('800x500')
    root.title('Справочник по людям')
    root.resizable(False, False)

    main_menu = Menu(root)
    root.config(menu=main_menu)

    file_menu = Menu(main_menu, tearoff=0)
    file_menu.add_command(label='Сохранить', command=save_table)
    file_menu.add_command(label='Закрыть', command=lambda: root.destroy())

    table_menu = Menu(main_menu, tearoff=0)
    table_menu.add_command(label="Добавить", command=add_wind)
    table_menu.add_command(label="Заменить", command=change_wind_1)
    table_menu.add_command(label="Удалить", command=del_wind)

    find_menu = Menu(main_menu, tearoff=0)
    find_menu.add_command(label="Найти", command=find_wind)
    find_menu.add_command(label="Результат поиска", command=show_find)

    main_menu.add_cascade(label="Файл", menu=file_menu)
    main_menu.add_cascade(label="Таблица", menu=table_menu)
    main_menu.add_cascade(label="Поиск", menu=find_menu)
    main_menu.add_command(label="Обновить страницу", command=show)

    text = Text(bg='white', width=97, height=100)
    text.pack(side=LEFT)
    scr = Scrollbar(command=text.yview)
    scr.pack(side=LEFT, fill=Y)
    text.config(yscrollcommand=scr.set)

    root.mainloop()


