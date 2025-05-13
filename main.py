import tkinter as tk
from tkinter import messagebox

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

def reset_window():
    global current_player, counter
    current_player = "X"
    counter = 0
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["bg"] = "white"

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

   if counter == 9:
       messagebox.showinfo("Игра окончена", f"Ничья")
       reset_window()

   current_player = "0" if current_player == "X" else "X"
   bg_button = "#9370DB" if bg_button == "#00FFFF" else "#00FFFF"


counter = 0
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=5, height=2, bg="white",  command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, sticky="nsew")
        window.grid_rowconfigure(j, weight=1)
        row.append(btn)
    window.grid_columnconfigure(i, weight=1)
    buttons.append(row)

button = tk.Button(window, text="reset", font=("Arial", 10), command=reset_window)
button.grid(row=3, column=1, pady=10, ipadx=20)

window.mainloop()

