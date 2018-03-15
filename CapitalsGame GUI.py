import Tkinter
import random
import tkMessageBox

window = Tkinter.Tk()

countryCapitals = {"Slovenia": "Ljubljana",
                   "Croatia": "Zagreb",
                   "Austria": "Vienna",
                   "Italy": "Rome",
                   "Hungary": "Budapest",
                   "Germany": "Berlin",
                   "France": "Paris",
                   "Spain": "Madrid",
                   "Czech Republic": "Prague",
                   "Greece": "Athens",
                   "United Kingdom": "London",
                   "Ireland": "Dublin",
                   "Poland": "Warsav",
                   "Bulgaria": "Sofia",
                   "Netherlands": "Amsterdam",
                   "Macedonia": "Skopje",
                   "Montenegro": "Podgorica",
                   "Denmark": "Copenhagen",
                   "Finland": "Helsinki",
                   "Serbia": "Belgrade",
                   "Russia": "Moscow",
                   "Portugal": "Lisbon",
                   "San Marino": "San Marino",
                   "Sweden": "Stockholm",
                   "Switzerland": "Bern",
                   "Turkey": "Ankara",
                   "Iceland": "Reykjavik",
                   "Norway": "Oslo",
                   "Slovakia": "Bratislava"
                   }

# Pick a random key-value pair from dictionary
def randomCountry():
    current = random.randint(0, len(countryCapitals) - 1)
    keys = countryCapitals.keys()
    return keys[current]

drzava = randomCountry()
capital = ""
greeting = Tkinter.Label(window, text="What is the capital of %s?  " % drzava)
greeting.pack()
points = 0

guess = Tkinter.Entry(window)
guess.pack()

# Check answer
def provjera():
    capital = countryCapitals[drzava]
    grad = guess.get()
    global points
    if grad.lower() == capital.lower():
        points += 1
        tkMessageBox.showinfo("Correct", "Congratulations!")
    else:
        points -= 1
        tkMessageBox.showwarning("Error", "The capital of %s is %s" % (drzava, capital))
    guess.delete(0, "end")
    new()

submit = Tkinter.Button(window, text="Submit", command=provjera)
submit.pack()

# New question!
def new():
    global drzava
    drzava = randomCountry()
    greeting.config(text="What is the capital of %s?  " % drzava)

another = Tkinter.Button(window, text="Another!", command=new)
another.pack()

window.mainloop()

print "You scored " + str(points) + " points."