import tkinter as tk

def calculate_inheritance():
    total_cash = float(enter1.get())
    num_shops = int(enter2.get())
    num_houses = int(enter3.get())
    land_in_canals = float(enter4.get())
    num_sons = int(enter5.get())
    num_daughters = int(enter6.get())
    num_widows = int(enter7.get())

    print("Total Cash:", total_cash)
    print("Number of Shops:", num_shops)
    print("Number of Houses:", num_houses)
    print("Number of canals:", land_in_canals)
    print("Number of sons:", num_sons)
    print("Number of daughters:", num_daughters)
    print("Number of widows:", num_widows)


window=tk.Tk()
window.title("Islamic Inheritance Calculator")
window.configure(bg="Sky Blue")

label1=tk.Label(window,text="Enter total cash:",padx=10,pady=5,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=1,column=0)
enter1=tk.Entry(window,fg="Blue",font=("Arial Black",12)).grid(row=1,column=1)

label2=tk.Label(window,text="Enter number of shops:",padx=15,pady=10,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=2,column=0)
enter2=tk.Entry(window,fg="Blue",font=("Arial Black",12)).grid(row=2,column=1)

label3=tk.Label(window,text="Enter number of house in Marlas:",padx=15,pady=10,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=3,column=0)
enter3=tk.Entry(window,fg="Blue",font=("Arial Black",12)).grid(row=3,column=1)

label4=tk.Label(window,text="Enter agricultural land (in canals):",padx=15,pady=10,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=4,column=0)
enter4=tk.Entry(window, fg="Blue", font=("Arial Black", 12)).grid(row=4,column=1)

label5=tk.Label(window,text="Enter number of son:",padx=15,pady=10,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=5,column=0)
enter5=tk.Entry(window, fg="Blue", font=("Arial Black", 12)).grid(row=5,column=1)

label6=tk.Label(window,text="Enter number of daughtes:",padx=15,pady=10,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=6,column=0)
enter6=tk.Entry(window, fg="Blue", font=("Arial Black", 12)).grid(row=6,column=1)

label7=tk.Label(window,text="Enter number of widows:",padx=15,pady=10,bg="Sky Blue",fg="BLack",font=("Arial Black",12)).grid(row=7,column=0)
enter7=tk.Entry(window, fg="Blue", font=("Arial Black", 12)).grid(row=7,column=1)

button=tk.Button(window,text="Submit",command= "amount",bg="Sky Blue",fg="BLack",font=("Arial Black",10))
button.grid(row=8,column=1)
window.geometry("800x600") 
window.mainloop()