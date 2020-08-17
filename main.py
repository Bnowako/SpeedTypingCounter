from tkinter import *
from tkinter import ttk
import time
import threading


def restart_method():
    print("dupa")
    t1.delete("1.0", END)
    t1.insert(INSERT, "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
    input_text.set("")

    global run_once, i, chars
    run_once = 0
    t.cancel()
    timer.set("1:00")
    i = 60

    chars = 0
    score.set(f'Twój wynik to: {chars}')

    e1.configure(state=NORMAL)


global run_once
run_once = 0

global chars
chars = 0


def event_handler(event):
    global run_once
    if run_once == 0:
        countdown()
        run_once = 1
    print(event.get())
    print(t1.get("1.0"))

    if str(event.get()) == str(t1.get("1.0")):
        input_text.set("")
        t1.delete("1.0")
        global chars
        chars += 1
        score.set(f'Twój wynik to: {chars}')


global i
i = 4


def countdown():
    global i
    print(i)
    if i == 0:
        e1.configure(state=DISABLED)
        return
    i -= 1
    timer.set(f'00:{i}')
    global t
    t = threading.Timer(1, countdown)
    t.start()


root = Tk()
root.title("Speedtyping test")

b1 = ttk.Button(root, text="RESTART", command=restart_method)
b1.grid(column=0, row=0, ipadx=100, ipady=50)


input_text = StringVar()
input_text.trace("w", lambda name, index, mode,
                 input_text=input_text: event_handler(input_text))
e1 = ttk.Entry(root, textvariable=input_text)
e1.grid(column=0, row=1)
print(e1.state)


l1 = ttk.Label(
    root, text="Program zacznie odliczanie  jak zaczniesz wpisywac.")
l1.grid(column=1, row=3)

score = StringVar()
score.set("Twój wynik to: ")
l3 = ttk.Label(
    root, textvariable=score)
l3.grid(column=0, row=2)

timer = StringVar()
timer.set("1:00")
l2 = ttk.Label(root, textvariable=timer)
l2.grid(column=1, row=0)

t1 = Text(root)
t1.insert(INSERT, "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.")
t1.grid(column=1, row=1, rowspan=2)

root.mainloop()
