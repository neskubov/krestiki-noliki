import tkinter as tk
from tkinter import ttk

# Создаем главное окно
root = tk.Tk()
root.title("Красивая кнопка и меню")
root.geometry("300x200")

# Создаем стиль для кнопки
style = ttk.Style()
style.configure("Custom.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="#4CAF50",
                padding=10)
style.map("Custom.TButton",
          background=[("active", "#45a049"), ("pressed", "#3e8e41")])

# Функция для обработки нажатия кнопки
def on_button_click():
    print("Кнопка нажата!")

# Создаем красивую кнопку
button = ttk.Button(root, text="Нажми меня", style="Custom.TButton", command=on_button_click)
button.pack(pady=20)

# Выпадающее меню
def on_menu_select(event):
    print(f"Вы выбрали: {combo.get()}")

# Создаем стиль для выпадающего меню
style.configure("TCombobox",
                padding=5,
                font=("Arial", 12))

options = ["Опция 1", "Опция 2", "Опция 3"]
combo = ttk.Combobox(root, values=options, style="TCombobox")
combo.set("Выбери опцию")  # Устанавливаем текст по умолчанию
combo.bind("<<ComboboxSelected>>", on_menu_select)
combo.pack(pady=20)

# Запуск главного цикла приложения
root.mainloop()