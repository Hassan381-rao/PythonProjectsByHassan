import tkinter as tk
from tkinter import*
window=tk.Tk()
window.resizable(0,0)
window.title("Calculator")
window.geometry("350x300")
data = StringVar()
val = ""

def btn_click(num):
    global val
    val=val+str(num)
    data.set(val)

def btn_clear():
    global val
    val=""
    data.set("")

def btn_equals():
 global val
 result = str(eval(val))
 data.set(result)

display = Entry(window, textvariable=data, justify=RIGHT, bd=20, bg='coral')
display.grid(row=0, column=0, columnspan=4)

btn7=Button(window,text="7",font=("Arial Black",12),height=2, width=6, command=lambda: btn_click(7))
btn7.grid(row=1, column=0)
btn8=Button(window,text="8",font=("Arial Black",12),height=2, width=6, command=lambda: btn_click(8))
btn8.grid(row=1, column=1)
btn9=Button(window,text="9",font=("Arial Black",12),height=2, width=6, command=lambda: btn_click(9))
btn9.grid(row=1, column=2)
btnadd=Button(window,text="+",font=("Arial Black",12),height=2, width=6, command=lambda: btn_click('+'))
btnadd.grid(row=1, column=3)

btn6 = Button(window, text='6', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(6))
btn6.grid(row=2, column=0) 
btn5 = Button(window, text='5', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(5))
btn5.grid(row=2, column=1)
btn4 = Button(window, text='4', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(4))
btn4.grid(row=2, column=2)
btnsub = Button(window, text='-', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click('-'))
btnsub.grid(row=2, column=3)

btn3 = Button(window, text='3', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(3))
btn3.grid(row=3, column=0)
btn2 = Button(window, text='2', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(2))
btn2.grid(row=3, column=1)
btn1 = Button(window, text='1', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(1))
btn1.grid(row=3, column=2)
btnmulti = Button(window, text='*', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click('*'))
btnmulti.grid(row=3, column=3)

btnc = Button(window, text='C', font=("Arial Black", 12), height=2, width=6, command=btn_clear)
btnc.grid(row=4, column=0)
btn0 = Button(window, text='0', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click(0))
btn0.grid(row=4, column=1)
btnequal = Button(window, text='=', font=("Arial Black", 12), height=2, width=6, command=btn_equals)
btnequal.grid(row=4, column=2)
btndivide = Button(window, text='/', font=("Arial Black", 12), height=2, width=6, command=lambda: btn_click('/'))
btndivide.grid(row=4, column=3)

window.mainloop()


