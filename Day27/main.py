# def add(*args):
#     print(args[0])
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
# print(add(4,5,6,7))
#
# def calculate(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])
#
# calculate(add=3, multiply=5)


# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add=3, multiply=5)


# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw["make"]
#         self.model = kw["model"]
#
#
# my_car = Car(make="Nissan", model="GT-R")
# print(my_car.model)


# class Car:
#
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#         self.colour = kw.get("colour")
#         self.seats = kw.get("seats")
# 
#
# my_car = Car(make="Nissan", model="skyline")
# print(my_car.make, my_car.model)


# import tkinter
#
# window = tkinter.Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
# #label
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 16, "bold"))
# my_label.pack(side="top")


# from tkinter import *
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
#
# #label
# my_label = Label(text="I am a Label", font=("Arial", 16, "bold"))
# my_label.pack(side="top")
#
# my_label["text"] = "NEW TEXT"
# my_label.config(text="New Text")
#
#
# #button
# def button_clicked():
#     print("I GOT CLICKED")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
# button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
#
# #Entry
#
# input = Entry(width=10)
# input.pack(side="left")
# print(input.get())
#
# window.mainloop()


# from tkinter import *
#
# #Creating a new window and configurations
# window = Tk()
# window.title("Widget Examples")
# window.minsize(width=500, height=500)
#
# #Labels
# label = Label(text="This is old text")
# label.config(text="This is new text")
# label.pack()
#
# #Buttons
# def action():
#     print("Do something")
#
# #calls action() when pressed
# button = Button(text="Click Me", command=action)
# button.pack()
#
# #Entries
# entry = Entry(width=30)
# #Add some text to begin with
# entry.insert(END, string="Some text to begin with.")
# #Gets text in entry
# print(entry.get())
# entry.pack()
#
# #Text
# text = Text(height=5, width=30)
# #Puts cursor in textbox.
# text.focus()
# #Adds some text to begin with.
# text.insert(END, "Example of multi-line text entry.")
# #Get's current value in textbox at line 1, character 0
# print(text.get("1.0", END))
# text.pack()
#
# #Spinbox
# def spinbox_used():
#     #gets the current value in spinbox.
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #Checkbutton
# def checkbutton_used():
#     #Prints 1 if On button checked, otherwise 0.
#     print(checked_state.get())
# #variable to hold on to checked state, 0 is off, 1 is on.
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton
# def radio_used():
#     print(radio_state.get())
# #Variable to hold on to which radio button value is checked.
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# #Listbox
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()
# window.mainloop()
#


# from tkinter import *
#
# window = Tk()
# window.title("My first GUI program")
# window.minsize(width=500, height=300)
# window.config(padx=50, pady=50)
#
# #label
# my_label = Label(text="I am a Label", font=("Arial", 16, "bold"))
# my_label.pack(side="top")
# my_label["text"] = "NEW TEXT"
# my_label.config(text="New Text")
# # my_label.place(x=100,y=200)
# my_label.grid(column=0,row=0)
#
#
# #button
# def button_clicked():
#     print("I GOT CLICKED")
#     new_text = input.get()
#     my_label.config(text=new_text)
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1,row=1)
#
# new_button = Button(text="new button")
# new_button.grid(column=3,row=1)
#
# #Entry
# input = Entry(width=10)
# print(input.get())
# input.grid(column=2,row=2)
#
# window.mainloop()


from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()