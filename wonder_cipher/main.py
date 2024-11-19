from tkinter import Tk
from tkinter import ttk
from tkinter.messagebox import showerror

import algorithms


def main():
    def do_cipher():
        """Запускает шифрование выбранным методом, обновляет результат"""
        if method.get() == "Цезарь":
            if not key.get().isdigit():
                showerror("Ошибка", "Ключ должен быть числом")
            else:
                shift = int(key.get())
                output.config(text=algorithms.run_cipher(text.get(), algorithms.ceaser, shift))
        elif method.get() == "Атбаш":
            output.config(text=algorithms.run_cipher(text.get(), algorithms.atbash, 0))
        elif method.get() == "Вижинер":
            if key.get() == "":
                showerror("Ошибка", "Ключ не должен быть пустым")
            else:
                output.config(text=algorithms.run_cipher(text.get(), algorithms.vinger, key.get()))
        else:
            showerror("Ошибка", "Неправильный шифр")


    def do_decipher():
        """Запускает дешифрование выбранным методом, обновляет результат"""
        if method.get() == "Цезарь":
            if not key.get().isdigit():
                showerror("Ошибка", "Ключ должен быть числом")
            else:
                shift = int(key.get())
                output.config(text=algorithms.run_cipher(text.get(), algorithms.anti_ceaser, shift))
        elif method.get() == "Атбаш":
            output.config(text=algorithms.run_cipher(text.get(), algorithms.atbash, 0))
        elif method.get() == "Вижинер":
            if key.get() == "":
                showerror("Ошибка", "Ключ не должен быть пустым")
            else:
                output.config(text=algorithms.run_cipher(text.get(), algorithms.anti_vinger, key.get()))
        else:
            showerror("Ошибка", "Неправильный шифр")


    root = Tk()
    root.title("Шифратор")
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    ttk.Label(frm, text="Текст: ").grid(column=0, row=0)
    text = ttk.Entry(frm)
    text.grid(column=1, row=0)

    ttk.Label(frm, text="Ключ: ").grid(column=0, row=1)
    key = ttk.Entry(frm)
    key.grid(column=1, row=1)

    ttk.Label(frm, text="Шифр: ").grid(column=0, row=2)
    method = ttk.Combobox(frm, values=["Цезарь", "Атбаш", "Вижинер"])
    method.grid(column=1, row=2)

    ttk.Button(frm, text="Шифровать", command=do_cipher).grid(column=0, row=3)
    ttk.Button(frm, text="Дешифровать", command=do_decipher).grid(column=1, row=3)

    ttk.Label(frm, text="Вывод: ").grid(column=0, row=4)
    output = ttk.Label(frm, text="Ты лапочка")
    output.grid(column=1, row=4)

    root.mainloop()


if __name__ == "__main__":
    main()