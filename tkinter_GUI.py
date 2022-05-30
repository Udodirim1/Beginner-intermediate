from tkinter import *
window = Tk()

#labels
Label(window, text= "What is your name?").grid(row = 0, column= 0)
Label(window, text= "How old are you?.").grid(row = 1, column= 0)

# Text Input
my_name = Entry(window, width= 50, borderwidth = 5)
my_name.grid(row = 0, column = 1)

my_age = Entry(window, width = 50, borderwidth = 5)
my_age.grid(row = 1, column = 1)

def on_click():
    print(f"My name is {my_name.get()}, and my age is... {my_age.get()}")

# Button widget
Button(window, text = "Click me", command = on_click ).grid(row = 2, column = 1)

#window.title("First Tkinter Window")


window.mainloop()