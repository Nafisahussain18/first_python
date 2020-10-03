import tkinter as tk
import os

# main
root = tk.Tk()

# create a fuction
# get( ): gets the value from the text box in the string formt


def calc_add():
    result = eval(a_text.get()) + eval(b_text.get())

    lbl_answer.configure(text="Answer : "+a_text.get()+" + " +
                         b_text.get() + " = " + str(result))


def clear_btn():
    a_text.delete(first=0, last=100)
    b_text.delete(first=0, last=100)
    a_text.focus()
    lbl_answer.configure(text="")


canvas = tk.Canvas(root, height=600, width=400, bg='#DAF7A6')
canvas.pack()
frame = tk.Frame(root, bg="#3D5A12")
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)
lbl_heading = tk.Label(
    frame, text="Addition of two Numbers", bg="#3D5A12", fg="black")
lbl_heading.place(x=80, y=20)


# label 1 : enter the value of a

lbl_a = tk.Label(frame, text="Enter the value of a", bg="#3D5A12", fg="black")
lbl_a.place(x=20, y=80)


# label 2 : enter the value of b

lbl_b = tk.Label(frame, text="Enter the value of b", bg="#3D5A12", fg="black")
lbl_b.place(x=20, y=120)

# text box,Entry()
a_text = tk.Entry(frame, width=20, bd=1)
a_text.place(x=150, y=80)

b_text = tk.Entry(frame, width=20, bd=1)
b_text.place(x=150, y=120)

# button ,Button
cal_btn = tk.Button(frame, text="Add", padx=20,
                    pady=10, bg="#23320E", fg="white", command=calc_add)
cal_btn.place(x=60, y=170)

clr_btn = tk.Button(frame, text="Clear", padx=20,
                    pady=10, bg="#23320E", fg="white", command=clear_btn)
clr_btn.place(x=180, y=170)


lbl_answer = tk.Label(
    frame, text="", bg="#3D5A12", fg="black")
lbl_answer.place(x=80, y=220)

root.mainloop()
