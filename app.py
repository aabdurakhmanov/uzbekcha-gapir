"""
    This is program for speach any text in uzbek
    Bu dastur istalgan matnni uzbek tilida talafuz qilib beraoladi
"""

import pyttsx3
from tkinter import *
from tkinter import filedialog

# create tkinter Desktop app
root = Tk()
root.title('text_to_speech')
root.geometry('1000x800')
root.iconbitmap('D:\™chromes™/text.ico')


# Function for speech in text
def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[2].id)
    engine.say(my_entry.get())

    engine.runAndWait()

    my_entry.delete(0,END)

# Function for speech to any text file
def talk_file():
    engine = pyttsx3.init()
    engine.setProperty('rate', 130)

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[2].id)
    engine.say(my_text.get("1.0",'end-1c'))

    engine.runAndWait()

# Function for open file
def open_file():
    text_file = filedialog.askopenfilename(
        initialdir='E:\Projects/text_tospeech_diplomwork/',
        title='Open file',
        filetypes=(('Text Files', '*.txt'),)
    )
    text_file = open(text_file, 'r')
    stuff = text_file.read()

    my_text.insert(END, stuff)
    text_file.close()

# Function for save file
def save_file():
    text_file = filedialog.askopenfilename(
        initialdir='E:/Projects/text_tospeech_diplomwork/',
        title='Open file',
        filetypes=(('Text Files', '*.txt'),)
    )
    text_file = open(text_file, 'w')
    text_file.write(my_text.get(1.0, END))


my_entry = Entry(root,
                 font=('Helvetica', 60)
                 )
my_entry.pack(pady=30)

# button_img = PhotoImage(width=1, height=1)
my_button = Button(root,
                   text='Listen',
                   command=talk,
                   compound='c',
                   font=('Impact', 20),
                   )

my_button.pack(pady=10)

# Open file place
my_text = Text(root,
               width=100,
               height=12,
               font=('Impact', 20, 'italic')
               )
my_text.pack(pady=20)

# Open file button
open_button = Button(root,
                     text='Open text file',
                     command=open_file
                     )
open_button.pack(pady=5)

# To talk file text to speech
speech_file_button = Button(root,
                            text='Speech text file',
                            command=talk_file
                            )
speech_file_button.pack(pady=5)

# File save if file changed
save_button = Button(root,
                     text='Save File',
                     command=save_file
                     )
save_button.pack(pady=5)

root.mainloop()
