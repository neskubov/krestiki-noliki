import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Пример расположения")
root.geometry("400x300")  # Устанавливаем размер окна

# Создаем виджеты
for row in range(3):  # Создаем первые 3 строки с пустыми "ячейками"
    for col in range(3):
        frame = tk.Frame(root, width=100, height=50, bg="lightgray", borderwidth=1, relief="solid")
        frame.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Четвертая строка с меткой и кнопками
label = tk.Label(root, text="Это метка", bg="yellow")
label.grid(row=3, column=1, sticky="e", padx=5, pady=5)  # Размещаем метку в 4-й строке, во втором столбце

button1 = tk.Button(root, text="Кнопка 1")
button1.grid(row=3, column=2, sticky="w", padx=5, pady=5)  # Размещаем кнопку 1 рядом с меткой

button2 = tk.Button(root, text="Кнопка 2")
button2.grid(row=4, column=1, columnspan=2, pady=5)  # Размещаем кнопку 2 под меткой и кнопкой 1, на 2 столбца

# Настраиваем размерность сетки
root.grid_columnconfigure([0, 1, 2], weight=1)  # Растяжение колонок
root.grid_rowconfigure([0, 1, 2, 3, 4], weight=1)  # Растяжение строк

# Запускаем главный цикл программы
root.mainloop()