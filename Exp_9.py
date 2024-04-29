import tkinter
from tkinter import *
t = tkinter.Tk()

# title of the window
t.title("Exp_9")

# Label
w = Label(t, text='Python Lab')
w.pack()

# Listbox
Lb = Listbox(t)
Lb.insert(1, '1')
Lb.insert(2, '2')
Lb.insert(3, '3')
Lb.insert(4, '4')
Lb.pack()

# Canvas
w = Canvas(t, width=40, height = 60)
w.pack()
Canvas_height=20
Canvas_width=200
y = int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)

# Button to end the process
button  = tkinter.Button(t, width=25, text='END', command=t.destroy)
button.pack()

# CheckBox
var1 = IntVar()
CheckButton(t, text='male', variable=var1)
var2 = IntVar()
CheckButton(t, text='female', variable=var2)

t.mainloop()
