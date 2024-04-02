import tkinter as tk
from tkinter import simpledialog
def say_hello():
    name = name_entry.get()
    # Вывод  сообщения с  приветствием
    greeting_label.config(text=f"Привет, {name}!")

root = tk.Tk()
root.title("   Приве---тствие")

name_entry = tk.Entry(root)
name_entry.pack(pady=10)

greet_button = tk.Button(root, text="Поздороваться", command=say_hello)
greet_button.pack(pady=5)


greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=10)


root.mainloop()
