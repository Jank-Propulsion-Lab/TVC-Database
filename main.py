from sqlite3 import Row
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *

from numpy import pad

LARGE_FONT = ("Verdand", 12)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, GraphPage, DataInject):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Jank Database Home")
        label.pack(padx=10, pady=10)
        graph = ttk.Button(self, text="Graphs", command= lambda: controller.show_frame(GraphPage))
        graph.pack()
        data = ttk.Button(self, text="Inject Data", command = lambda: controller.show_frame(DataInject))
        data.pack()

class GraphPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Graphs")
        label.pack(padx=10, pady=10)
        home = ttk.Button(self, text="Home", command=lambda: controller.show_frame(StartPage))
        home.pack()
        data = ttk.Button(self, text="Inject Data", command=lambda: controller.show_frame(DataInject))
        data.pack()

class DataInject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Inject Data")
        label.pack(padx=10, pady=10)
        home = ttk.Button(self, text="Home", command = lambda: controller.show_frame(StartPage))
        home.pack()
        graph = ttk.Button(self, text="Graphs", command = lambda: controller.show_frame(GraphPage))
        graph.pack()

app = App()
app.title("Jank Database")
app.geometry("1280x720")
theme = ttk.Style(app)
theme.theme_use('alt')
app.mainloop()