import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Enter a number to fizzbuzz up to!")
greeting.pack()

number = Tkinter.Entry(window)
number.pack()

def fizzItOut():
    countTo = int(number.get())
    string = ""
    buzzItIN = []

    for x in range(countTo):
        if ((x+1) % 3) == 0:
            string = string + "fizz"
        if ((x+1) % 5) == 0:
            string = string + "buzz"
        if (((x+1) % 3) != 0) and (((x+1) % 5) != 0):
            buzzItIN.append(x + 1)
        else:
            buzzItIN.append(string)
        string = ""

    tkMessageBox.showinfo("FizzBuzzing Finshed", buzzItIN)
    number.delete(0, "end")

submit = Tkinter.Button(window, text="Submit", command=fizzItOut)  # check_guess, not check_guess()
submit.pack()
window.mainloop()