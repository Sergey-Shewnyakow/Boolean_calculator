import itertools
from tkinter import *
import tkinter as tk
from tkinter import ttk

alphabet = ['a', 'b', 'c' ,'d']
def sort_column(treeview, col, reverse):
    l = [(treeview.set(k, col), k) for k in treeview.get_children('')]
    l.sort(reverse=reverse)

    for index, (val, k) in enumerate(l):
        treeview.move(k, '', index)

    treeview.heading(col, command=lambda: sort_column(treeview, col, not reverse))
def bulen_calculator(ent):
    if ent == "":     #условие если поступила пустая строка
        error = Tk()
        error.title("error")
        error.geometry("250x200")
        label = tk.Label(error, text="Введите что-нибудь в строку :)")
        label.pack(anchor=CENTER, expand=1)

    else:
        new_w = tk.Tk()
        new_w.geometry(f"700x400")
        new_w.title("Table")

        style = ttk.Style()
        style.theme_use('default')
        style.configure("St.Treeview", font=("Arial", 12), background='#000000', fieldbackground='#000000',
                      foreground='white')
        style.configure("St.Treeview.Heading", font=("Arial", 14), foreground='white')

        original_str = ent
        expression = ent
        expression = expression.replace("∧", " and ").replace("∨", " or ").replace("¬", " not ").replace("→"," <= ")\
            .replace("≡", " == ")
        variables = sorted(list(
            set(expression.replace("(", "").replace(")", "").replace("not", "").replace("and", "").
                replace("or","").replace(" ", "").replace("<=","").replace("==","").replace("0", "").replace("1",""))))
        columns = variables.copy()
        columns.append(original_str)

        tree = ttk.Treeview(new_w, columns=columns, show='headings', style = "St.Treeview")
        tree.tag_configure('result_true', background='#C9FF9E')
        tree.tag_configure('result_false', background='#FF9EA5')

        for row in columns:
            tree.heading(row, text=str(row), anchor= CENTER)
            tree.column(row, anchor=CENTER)
        tree.heading(str(original_str), text=str(original_str))

        values = list(itertools.product([True, False], repeat=len(variables)))

        for col in columns:
            tree.heading(col, text=col, command=lambda c=col: sort_column(tree, c, False))

        for value in values:
            value_dict = {variables[i]: value[i] for i in range(len(variables))}
            result = eval(expression, value_dict)
            value_str = " ".join([str(v) for v in value])
            temp_per3 = (str(value_str + " " + str(result)))
            temp_per3 = temp_per3.replace("True", "1").replace("False", "0")
            if (result):
                tree.insert("", END, values=temp_per3, tags=('result_true'))
            else:
                tree.insert("", END, values=temp_per3, tags=('result_false'))


        tree.pack(fill=tk.BOTH, expand=True)
        ttk.Button(new_w, text="a")

        new_w.mainloop()

def calculate():
    expression = entry.get()
    bulen_calculator(expression)


def enter(event):
    expression = entry.get()
    bulen_calculator(expression)


def add_digit(symbol):
    end_str = entry.get() + symbol
    entry.delete(0, tk.END)
    entry.insert(0, end_str)


def add_button():
    symbol = alphabet[0]
    num = 0
    if 'a' not in alphabet:
        num = 1
    if 'b' not in alphabet:
        num = 2
    if 'c' not in alphabet:
        num = 3
    if 'd' not in alphabet:
        num = 4
    alphabet.pop(0)
    ttk.Button(text=symbol, command= lambda: add_digit(symbol), style = 'my.TButton').grid(row=6, column=num, stick='wens')


def clear():
    entry.delete(0, tk.END)


def delete():
    end_str = entry.get()[0:-1]
    entry.delete(0, tk.END)
    entry.insert(0, end_str)


window = tk.Tk()
window.geometry(f"540x730")
window.title("Boolean Calculator")
window['bg'] = "#FFFFFF"
window.resizable(True, True)
window.bind('<Return>', enter)
for i in range(4):
    window.grid_columnconfigure(i, weight=1)
for i in range(6):
    window.grid_rowconfigure(i, weight=1)



# стиль кнопок
style = ttk.Style()
style.theme_use('default')

style.configure('my.TButton', font=('Arial', 12), foreground='#FFFFFF', background='#666666')
style.map('my.TButton', background=[('active', '#FF8C00')])
style.configure('my.TButton', relief='flat', borderwidth=1)
style.configure('my.TButton', padding=(10, 5))
style.configure('my.TButton', cursor='hand2')

def adapt_font_size(event):  #адаптивный текст в строке ввода
    font_size = max(int(window.winfo_height() / 20), 8)
    entry.config(font=('Arial', font_size))


entry = tk.Entry(window, font=('Arial', 10), bg= "#FFFFFF", fg='#363636')
entry.grid(row=0, column=0, columnspan=4, sticky='wens')

window.bind('<Configure>', adapt_font_size)


#кнопки для опираций
button = ttk.Button(window, text="CALCULATE", command= lambda: [calculate()], style = 'my.TButton')
button.grid(row =2, column= 3, rowspan= 3, stick = 'wens')

ttk.Button(text="∧(and)", command= lambda: add_digit("∧"), style = 'my.TButton').grid(row = 1, column= 0, stick = 'wens')
ttk.Button(text="∨(or)", command= lambda: add_digit("∨"),style = 'my.TButton').grid(row = 2, column= 0, stick = 'wens')
ttk.Button(text="¬(not)", command= lambda: add_digit("¬"), style = 'my.TButton').grid(row = 3, column= 0, stick = 'wens')
ttk.Button(text="≡", command= lambda: add_digit("≡"), style = 'my.TButton').grid(row = 4, column= 0, stick = 'wens')
ttk.Button(text="→", command= lambda: add_digit("→"), style = 'my.TButton').grid(row = 5, column= 0, stick = 'wens')
ttk.Button(text="X", command= lambda: add_digit("x"), style = 'my.TButton').grid(row = 1, column= 1, stick = 'wens')
ttk.Button(text="Y", command= lambda: add_digit("y"), style = 'my.TButton').grid(row = 2, column= 1, stick = 'wens')
ttk.Button(text="Z", command= lambda: add_digit("z"), style = 'my.TButton').grid(row = 3, column= 1, stick = 'wens')
ttk.Button(text="W", command= lambda: add_digit("w"), style = 'my.TButton').grid(row = 4, column= 1, stick = 'wens')
ttk.Button(text="(", command= lambda: add_digit("("), style = 'my.TButton').grid(row = 1, column= 2, stick = 'wens')
ttk.Button(text=")", command= lambda: add_digit(")"), style = 'my.TButton').grid(row = 2, column= 2, stick = 'wens')
ttk.Button(text="1", command= lambda: add_digit("1"), style = 'my.TButton').grid(row = 3, column= 2, stick = 'wens')
ttk.Button(text="0", command= lambda: add_digit("0"), style = 'my.TButton').grid(row = 4, column= 2, stick = 'wens')


ttk.Button(text="NEW VARIABLE ", command= lambda: add_button(), style = 'my.TButton').grid(row = 5, column= 1, columnspan=2, stick = 'wens')
ttk.Button(text="CLEAR", command= lambda: clear(), style = 'my.TButton').grid(row = 5, column= 3, stick = 'wens')
ttk.Button(text="DELETE", command= lambda: delete(), style = 'my.TButton').grid(row = 1, column= 3, stick = 'wens')



window.mainloop()

