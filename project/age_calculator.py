#!/usr/bin/env python3
import datetime
from tkinter import *
from PIL import Image
from PIL import ImageTk

root = Tk()
root.geometry("340x420")
root.title(" Age Calculator App ")

name = Label(text = "Name")
name.grid(column=0, row=1)
year = Label(text = "Year")
year.grid(column=0, row=2)
month = Label(text = "Month")
month.grid(column=0, row=3)
date = Label(text = "date")
date.grid(column=0, row=4)

nameEntry = Entry()
nameEntry.grid(column=1, row=1)
yearEntry = Entry()
yearEntry.grid(column=1, row=2)
monthEntry = Entry()
monthEntry.grid(column=1, row=3)
dateEntry = Entry()
dateEntry.grid(column=1, row=4 )

def getInput():
	name = nameEntry.get()
	user = Person(name, datetime.date(int(yearEntry.get()),int(monthEntry.get()),int(dateEntry.get())))
	textArea = Text(height=10, width=25)
	textArea.grid(column=1, row=6)
	answer = "Heyy {user}!!!. You are {age} years old!!!".format(user=name, age=user.age())
	textArea.insert(END, answer)

button = Button(root, text="Calculate Age", command=getInput, bg="Pink")
button.grid(column=1, row=5)

class Person:
	def __init__(self,name,birthdate):
		self.name = name
		self.birthdate = birthdate
	def age(self):
		today = datetime.date.today()
		age = today.year-self.birthdate.year
		return age

image = Image.open("ec2.jpeg")
image.thumbnail((300,300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = Label(image=photo)
label_image.grid(column=1, row=0)

root.mainloop()
