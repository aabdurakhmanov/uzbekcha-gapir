import tkinter as tk


class MainWindow:
    def __init__(self, master):
        self.master = master

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.label = tk.Label(self.frame, text = 'Scrol bla bla')
        self.label.pack()

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side = tk.RIGHT, fill = tk.Y)

        self.text = tk.Text(self.frame, yscrollcommand = self.scrollbar.set)
        self.text.pack()

        self.scrollbar.config(command = self.text.yview)


root = tk.Tk()
window = MainWindow(root)
root.mainloop()


# import docx
#
# # create an instance of a word document
# doc = docx.Document()
#
# # add a heading of level 0 (largest heading)
# doc.add_heading('Heading for the document', 0)
#
# # add a paragraph and store
# # the object in a variable
# doc_para = doc.add_paragraph('Your paragraph goes here, ')
#
# # add a run i.e, style like
# # bold, italic, underline, etc.
# doc_para.add_run('hey there, bold here').bold = True
# doc_para.add_run(', and ')
# doc_para.add_run('these words are italic').italic = True
#
# # add a page break to start a new page
# doc.add_page_break()
#
# # add a heading of level 2
# doc.add_heading('Heading level 2', 2)
#
# # pictures can also be added to our word document
# # width is optional
# doc.add_picture('path_to_picture')
#
# # now save the document to a location
# doc.save('path_to_document')
#
#
# # """
# #     This is program for speach any text in uzbek
# #
# # """
# #
# #
# # import pyttsx3
# # from tkinter import *
# # from tkinter import filedialog
# #
# #
# # # create tkinter Desktop app
# # root = Tk()
# # root.title('text_to_speech')
# # root.geometry('1366x710')
# # root.iconbitmap('D:\™chromes™/text.ico')
# # root.resizable(True, True)
# #
# # bg = PhotoImage(file="images/splash.png")
# # my_label = Label(root, image=bg)
# # my_label.place(x=0, y=0, relwidth=1, relheight=1)
# #
# #
# #
# # # Function for speech in text
# #
# # def talk():
# #     engine = pyttsx3.init()
# #     engine.setProperty('rate', 130)
# #
# #     voices = engine.getProperty('voices')
# #
# #     engine.setProperty('voice', voices[2].id)
# #     engine.say(my_entry.get())
# #
# #     engine.runAndWait()
# #
# #     my_entry.delete(0,END)
# #
# #
# #
# # # Function for speech to any text file
# #
# # def talk_file():
# #     global my_text
# #     engine = pyttsx3.init()
# #     engine.setProperty('rate', 130)
# #
# #     voices = engine.getProperty('voices')
# #
# #     engine.setProperty('voice', voices[2].id)
# #     engine.say(my_text.get("1.0",'end-1c'))
# #
# #     engine.runAndWait()
# #
# #
# #
# # # Function for open file
# #
# # def open_file():
# #     text_file = filedialog.askopenfilename(
# #         initialdir='E:\Projects/text_tospeech_diplomwork/',
# #         title='Open file',
# #         filetypes=(('Text Files', '*.txt'))
# #     )
# #     text_file = open(text_file, 'r')
# #     stuff = text_file.read()
# #
# #     my_text.insert(END, stuff)
# #     text_file.close()
# #
# #
# #
# #
# # # Function for save file
# #
# # def save_file():
# #     text_file = filedialog.askopenfilename(
# #         initialdir='E:/Projects/text_tospeech_diplomwork/',
# #         title='Open file',
# #         filetypes=(('Text Files', '*.txt'),)
# #     )
# #     text_file = open(text_file, 'w')
# #     text_file.write(my_text.get(1.0, END))
# #
# #
# # my_entry = Entry(
# #                  root,
# #                  font=('Helvetica', 90)
# #                  )
# # my_entry.pack(pady=20)
# #
# #
# #
# # # button_img = PhotoImage(width=1, height=1)
# #
# # my_button = Button(
# #                    root,
# #                    text='Listen',
# #                    command=talk,
# #                    compound='c',
# #                    font=('Helvetica', 12),
# #                    )
# #
# # my_button.pack(pady=10)
# # my_button.place(
# #                 anchor="nw",
# #                 x=650,
# #                 y=165,
# # )
# #
# #
# #
# # # Open file place
# # def textt():
# #    scrollbar = Scrollbar(root)
# #    scrollbar.pack(side=RIGHT, fill=Y)
# #    my_text = Text(
# #                   root,
# #                   width=95,
# #                   height=12,
# #                   bg='silver',
# #                   font=('Impact', 20, 'italic'),
# #                   )
# #    my_text.pack(pady=20)
# #
# #    my_text.config(yscrollcommand=scrollbar.set)
# #    scrollbar.config(command=my_text.yview)
# #
# # textt()
# # """
# #  Button for open text file
# # """
# #
# # open_button = Button(
# #                      root,
# #                      text='Open text file',
# #                      command=open_file
# #                      )
# # open_button.pack(pady=5)
# # open_button.place(
# #             x=550,
# #             y=620
# # )
# #
# #
# #
# # # To talk file text to speech
# #
# # speech_file_button = Button(
# #                             root,
# #                             text='Speech text file',
# #                             command=talk_file
# #                             )
# # speech_file_button.pack(pady=5)
# # speech_file_button.place(
# #                          x=650,
# #                          y=620
# # )
# #
# #
# #
# # # File save if file changed
# #
# # save_button = Button(
# #                      root,
# #                      text='Save File',
# #                      command=save_file
# #                      )
# # save_button.pack(pady=5)
# # save_button.place(
# #                   x=760,
# #                   y=620
# # )
# #
# #
# # root.mainloop()
# #
# # #
# # # from tkinter import *
# # #
# # # root = Tk()
# # # scrollbar = Scrollbar(root)
# # # scrollbar.pack( side = RIGHT, fill = Y )
# # #
# # # mylist = Listbox(root, yscrollcommand = scrollbar.set )
# # # for line in range(100):
# # #    mylist.insert(END, "This is line number " + str(line))
# # #
# # # mylist.pack( side = RIGHT, fill = BOTH )
# # # scrollbar.config( command = mylist.yview )
# # #
# # # mainloop()
# # #
# # # # from tkinter import *
# # # #
# # # # ws = Tk()
# # # # ws.title('PythonGuides')
# # # # ws.geometry('400x300')
# # # # ws.config(bg='#F25252')
# # # #
# # # # frame = Frame(ws)
# # # #
# # # # text_box = Text(
# # # #     ws,
# # # #     height=13,
# # # #     width=32,
# # # #     font=(12)
# # # # )
# # # #
# # # # text_box.pack(side=LEFT,expand=True)
# # # #
# # # #
# # # # sb_ver = Scrollbar(
# # # #     ws,
# # # #     orient=VERTICAL
# # # #     )
# # # #
# # # # sb_ver.pack(side=RIGHT, fill=Y)
# # # #
# # # # text_box.config(yscrollcommand=sb_ver.set)
# # # # sb_ver.config(command=text_box.yview)
# # # #
# # # #
# # # # ws.mainloop()
# # # # import tkinter
# # # # import tkinter.ttk as ttk
# # # #
# # # # class TextScrollCombo(ttk.Frame):
# # # #
# # # #     def __init__(self, *args, **kwargs):
# # # #
# # # #         super().__init__(*args, **kwargs)
# # # #
# # # #     # ensure a consistent GUI size
# # # #         self.grid_propagate(False)
# # # #     # implement stretchability
# # # #         self.grid_rowconfigure(0, weight=1)
# # # #         self.grid_columnconfigure(0, weight=1)
# # # #
# # # #     # create a Text widget
# # # #         self.txt = tkinter.Text(self)
# # # #         self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
# # # #
# # # #     # create a Scrollbar and associate it with txt
# # # #         scrollb = ttk.Scrollbar(self, command=self.txt.yview)
# # # #         scrollb.grid(row=1, column=2, sticky='nsew')
# # # #         self.txt['yscrollcommand'] = scrollb.set
# # # #
# # # # main_window = tkinter.Tk()
# # # #
# # # # combo = TextScrollCombo(main_window)
# # # # combo.pack(fill="both", expand=False)
# # # # combo.config(width=600, height=600)
# # # #
# # # # combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
# # # # combo.txt.config(borderwidth=3, relief="sunken")
# # # #
# # # # style = ttk.Style()
# # # # style.theme_use('clam')
# # # #
# # # # main_window.mainloop()