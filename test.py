import tkinter as tk
from tkinter import Label, Toplevel, Radiobutton, StringVar, OptionMenu, messagebox, ttk

window = tk.Tk()
window.title("Крестики-нолики")

# Получаем размеры экрана
window_width = 400
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.configure(bg="lightblue")

current_player = "X"
bg_button = "#9370DB"

style = ttk.Style()
style.configure("Custom.TButton",
                font=("Arial", 8),
                foreground="black",
                background="#FFA500")
style.map("Custom.TButton",
          background=[("active", "#45a049"), ("pressed", "#3e8e41")])


style.configure("TCombobox",
                font=("Arial", 8))


def on_menu_select(event):
    global current_player
    current_player = combo.get()


def update_score(player):
    global player1_score, player2_score
    if player == 1:
        player1_score += 1
    elif player == 2:
        player2_score += 1


def check_winner():
   for i in range(3):
       if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
           return True
       if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
           return True

   if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
       return True
   if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
       return True

   return False


def on_click(row, col):
   global current_player, counter, bg_button

   counter += 1

   if buttons[row][col]['text'] != "":
       return

   buttons[row][col]['bg'] = bg_button
   buttons[row][col]['text'] = current_player

   if check_winner():
       messagebox.showinfo("Игра окончена",f"Игрок {current_player} победил!")
       reset_window()
       return

   if counter == 9:
       messagebox.showinfo("Игра окончена", f"Ничья")
       reset_window()
       return

   current_player = "0" if current_player == "X" else "X"
   bg_button = "#9370DB" if bg_button == "#00FFFF" else "#00FFFF"


def reset_window():
    global current_player, counter
    current_player = combo.get()
    counter = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["bg"] = "white"


counter = 0
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=8, height=2, bg="white",  command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, sticky="nsew")
        window.grid_rowconfigure(j, weight=1)
        row.append(btn)
    window.grid_columnconfigure(i, weight=1)
    buttons.append(row)

frame_options = tk.Frame(window, bg="lightblue")
frame_options.grid(row=3, column=1, rowspan=3, sticky="nsew")
frame_options.grid_columnconfigure(0, weight=1)  # Настройка столбца

label = Label(frame_options, text="Начинает:", bg="lightblue")
label.grid(row=3, sticky="ew", padx=5, pady=5)

options = ["X", "0"]
combo = ttk.Combobox(frame_options, values=options, style="TCombobox", state="readonly")
combo.set(options[0])  # Устанавливаем текст по умолчанию
combo.bind("<<ComboboxSelected>>", on_menu_select)
combo.grid(row=4, sticky="ew", padx=5, pady=5)

button = ttk.Button(frame_options, style="Custom.TButton", text="Сброс", command=reset_window)
button.grid(row=5, pady=10, sticky="ew", padx=5)


score1 = tk.Frame(window, bg="lightblue")
score1.grid(row=3, column=0, rowspan=3, sticky="nsew")

score2 = tk.Frame(window, bg="lightblue")
score1.grid(row=3, column=2, rowspan=3, sticky="nsew")


window.mainloop()

