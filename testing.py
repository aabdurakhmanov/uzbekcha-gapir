from tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = RIGHT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()

# from tkinter import *
#
# ws = Tk()
# ws.title('PythonGuides')
# ws.geometry('400x300')
# ws.config(bg='#F25252')
#
# frame = Frame(ws)
#
# text_box = Text(
#     ws,
#     height=13,
#     width=32,
#     font=(12)
# )
#
# text_box.pack(side=LEFT,expand=True)
#
#
# sb_ver = Scrollbar(
#     ws,
#     orient=VERTICAL
#     )
#
# sb_ver.pack(side=RIGHT, fill=Y)
#
# text_box.config(yscrollcommand=sb_ver.set)
# sb_ver.config(command=text_box.yview)
#
#
# ws.mainloop()
# import tkinter
# import tkinter.ttk as ttk
#
# class TextScrollCombo(ttk.Frame):
#
#     def __init__(self, *args, **kwargs):
#
#         super().__init__(*args, **kwargs)
#
#     # ensure a consistent GUI size
#         self.grid_propagate(False)
#     # implement stretchability
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)
#
#     # create a Text widget
#         self.txt = tkinter.Text(self)
#         self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)
#
#     # create a Scrollbar and associate it with txt
#         scrollb = ttk.Scrollbar(self, command=self.txt.yview)
#         scrollb.grid(row=1, column=2, sticky='nsew')
#         self.txt['yscrollcommand'] = scrollb.set
#
# main_window = tkinter.Tk()
#
# combo = TextScrollCombo(main_window)
# combo.pack(fill="both", expand=False)
# combo.config(width=600, height=600)
#
# combo.txt.config(font=("consolas", 12), undo=True, wrap='word')
# combo.txt.config(borderwidth=3, relief="sunken")
#
# style = ttk.Style()
# style.theme_use('clam')
#
# main_window.mainloop()