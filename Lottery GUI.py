import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Welcome to the Lottery numbers generator.\n Please enter how many random numbers would you like to have:")
greeting.pack()

howManyNumbers = Tkinter.Entry(window)
howManyNumbers.pack()

def randomize():
    list = []
    quantity = howManyNumbers.get()
    while True:
        if len(list) == int(quantity):
            break
        newNumber = random.randint(1, 100)
        if newNumber not in list:
            list.append(newNumber)
    #return list
    tkMessageBox.showinfo("Lottery Numbers", list)
    howManyNumbers.delete(0, "end")

submit = Tkinter.Button(window, text="Submit", command=randomize)  # check_guess, not check_guess()
submit.pack()

window.mainloop()