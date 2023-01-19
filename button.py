import tkinter as tk
import random
import time

window = tk.Tk()
window.geometry("300x300")

# change_time = time.time()

# function for changing color named - change_color
def change_color(color=None):
    global change_time
    if color is None:
        color = random.choice(["red", "blue", "yellow", "orange", "pink"])
    button.config(bg=color)
    change_time = time.time()


def chek():
    global change_time, counter
    if button['bg'] != "red":
        counter += 1
        result_time.config(text=random.choice(["Oops!", "Not today!",
                                               "Good luck next time!"]))
    else:
        result_time.config(
            text=f"{round(time.time() - change_time, 4)}s")
        change_color("green")


# button which changes the color
button = tk.Button(
    text="Click me!",
    bg="blue",
    width=10,
    height=1,
    command=chek
)


# label для отображения времени на нажатие,
result_time = tk.Label(
    text="0.0s",
    foreground="green",
    font=("Arial", 25)
)


# и label ждя отображения количества ошибок
fails = tk.Label(
    foreground="red",
    font=("Arial", 25),
    text="0 Fails"
)


# при помощи данного цикла мы просто добавляем все наши елементы в окно
for c in window.children:
    window.children[c].pack()


counter = 0  # и определим переменную которая будет отвечать за количество ложных нажатий
def loop():
    fails.config(
        text=f"{counter} Fails")
    wait = [int(random.random() * 1000), int(random.random() * 1000)]
    window.after(min(wait), change_color)
    window.after(max(wait), loop)


window.after(2000, loop)
window.mainloop()