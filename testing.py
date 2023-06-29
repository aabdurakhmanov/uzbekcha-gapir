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


# # # # combo.txt.config(borderwidth=3, relief="sunken")
# # # #
# # # # style = ttk.Style()
# # # # style.theme_use('clam')
# # # #
# # # # main_window.mainloop()
