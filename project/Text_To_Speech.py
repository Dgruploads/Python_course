#!/usr/bin/env python3
from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x360")
root.configure(bg='ghost white')
Title = root.title("Python-Project - Text To Speech")

text_to_speech_label = Label(root, text="Text_To_Speech", font="arial 20 bold", bg="white smoke")
text_to_speech_label.pack()
Label(text="Python-Project", font="arial 15 bold", bg="white smoke",width='20').pack(side='bottom')


message = StringVar()
Label(root, text="Enter Text", font="arial 15 bold", bg="white smoke").place(x=20,y=60)

entry_field = Entry(root, textvariable = message, width = '50')
entry_field.place(x=20,y=100)

def Text_To_Speech():
	Message = entry_field.get()
	speech = gTTS(text = Message)
	speech.save("Python-Project.mp3")
	playsound("Python-Project.mp3")

def Exit():
	root.destroy()

def Reset():
	message.set("")

Button(root, text="PLAY", font="arial 15 bold", command=Text_To_Speech, width="4").place(x=25,y=140)
Button(root, text="EXIT", font="arial 15 bold", command=Exit, width="4", bg="OrangeRed1").place(x=100,y=140)
Button(root, text="RESET", font="arial 15 bold", command=Reset, width="6").place(x=175,y=140)

root.mainloop()
