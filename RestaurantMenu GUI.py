import Tkinter
import tkMessageBox

window = Tkinter.Tk()

greeting = Tkinter.Label(window, text="Enter todays meal: ")
greeting.pack()
meal = Tkinter.Entry(window)
meal.pack()
greeting2 = Tkinter.Label(window, text="Enter its price: ")
greeting2.pack()
price = Tkinter.Entry(window)
price.pack()
file = open("menu.txt", "w+")

def menuToday():
    menu = {}
    dish = meal.get()
    cost = price.get()

    menu[dish] = cost + " kn"
    file = open("menu.txt", "a")
    file.write(dish + " " + str(menu[dish]) + "\n")
    file.close()
    meal.delete(0, "end")
    price.delete(0, "end")

submit = Tkinter.Button(window, text="Submit", command=menuToday)  # check_guess, not check_guess()
submit.pack()

window.mainloop()

