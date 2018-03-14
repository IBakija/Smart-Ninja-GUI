import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Unesi prvi broj: ")
greeting.pack()
prvi = Tkinter.Entry(window)
prvi.pack()
greeting2 = Tkinter.Label(window, text="Unesi drugi broj: ")
greeting2.pack()
drugi = Tkinter.Entry(window)
drugi.pack()
greeting3 = Tkinter.Label(window, text="Unesi matematicku operaciju: ")
greeting3.pack()
operacija = Tkinter.Entry(window)
operacija.pack()
def izracunaj():
    x = int(prvi.get())
    y = int(drugi.get())
    math = operacija.get()
    if math == "+":
        result = x + y
        tkMessageBox.showinfo("Result","x + y = " + str(result))
    elif math == "-":
        result = x - y
        tkMessageBox.showinfo("Result","x - y = " + str(result))
    elif math == "*":
        result = x * y
        tkMessageBox.showinfo("Result","x * y = " + str(result))
    elif math == "/":
        result = x / y
        tkMessageBox.showinfo("Result","x / y = " + str(result))
    else:
        tkMessageBox.showerror("Error", "Unesite ispravnu operaciju ( +, -, *, /)")

    prvi.delete(0, "end")
    drugi.delete(0, "end")
    operacija.delete(0, "end")

submit = Tkinter.Button(window, text="Submit", command=izracunaj)  # check_guess, not check_guess()
submit.pack()
window.mainloop()