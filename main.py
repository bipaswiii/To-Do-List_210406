import pickle
from tkinter import *
from tkinter.font import Font
import tkinter.messagebox
from tkinter import filedialog
import sqlite3
root=Tk()
root.title("Bipaswi_Todo List")
root.geometry("500x800")
root.resizable(False,False)

    #Font
my_font=Font(
    family="Brush Script MT",
    size=30,
    weight="bold",)

    #Created frame
my_frame=Frame(root,)
my_frame.pack(pady=10)

#Listbox making
my_list= Listbox(my_frame,
                 font=my_font,
                 width=25,
                 height=5,
                 bg="SystemButtonFace",
                 bd=0,
                 fg="#464646",
                 highlightthickness=0,
                 selectbackground="#A6A6A6",
                 activestyle="none")
my_list.pack(side=LEFT,fill=BOTH)
# Creating ScrollBar
my_scrollbar=Scrollbar(my_frame,)
my_scrollbar.pack(side=RIGHT,fill=BOTH)

    #add scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

    #Creating Entrybox
my_entry=Entry(root,font=("Helvetica",24),width=26,)
my_entry.pack(pady=20)

    #Creating button frame
button_frame=Frame(root)
button_frame.pack(pady=20)














mainloop()

