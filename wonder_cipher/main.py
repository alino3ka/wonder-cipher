from tkinter import Tk
from tkinter import ttk
from tkinter.messagebox import showerror

from wonder_cipher.algorithms import Caesar, Atbash, Vigenere, Cipher


def _with_label(frm, row, label, entry):
    """Добавляет `entry` с пояснительным текстом на строку `row`"""
    ttk.Label(frm, text=label).grid(column=0, row=row)
    entry.grid(column=1, row=row)
    return entry


def _catch_error(f):
    """Перехватывает все ошибки и показывает их пользователю"""
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            showerror("Exception", str(e))
    return wrapper


def main():
    def run_method(action):
        @_catch_error
        def wrapper():
            if method.get() == "Цезарь":
                try:
                    caesar_key = int(key.get())
                except ValueError:
                    raise ValueError("key must be integer value")
                cipher = Caesar(caesar_key)
            elif method.get() == "Атбаш":
                cipher = Atbash()
            elif method.get() == "Вегенер":
                cipher = Vigenere(key.get())
            else:
                raise ValueError(f"undefined cipher method: {method.get()}")
            output.config(text=action(cipher, text.get()))
        return wrapper


    root = Tk()
    root.title("Шифратор")
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    text = _with_label(frm, 0, "Текст:", ttk.Entry(frm))
    key = _with_label(frm, 1, "Ключ:", ttk.Entry(frm))
    method = _with_label(
        frm, 2, "Шифр:",
        ttk.Combobox(frm, values=["Цезарь", "Атбаш", "Вегенер"]))
    ttk.Button(frm, text="Шифровать", command=run_method(Cipher.cipher)).grid(column=0, row=3)
    ttk.Button(frm, text="Дешифровать", command=run_method(Cipher.decipher)).grid(column=1, row=3)
    output = _with_label(frm, 4, "Вывод:", ttk.Label(frm, text="Ты лапочка"))

    root.mainloop()


if __name__ == "__main__":
    main()