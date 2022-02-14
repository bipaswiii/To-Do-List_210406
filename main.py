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

    #Database Creation
conn= sqlite3.connect('todolist.db')
#making cursor
c = conn.cursor()
#Create table
'''
c.execute("""CREATE TABLE TodoWorks(

       To_do text
        )""")
'''



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

    #FUNCTIONS
def delete_item():

    my_list.delete(ANCHOR)

def delete_db():
    # connecting database
    conn = sqlite3.connect('todolist.db')
    # Creating cursor
    c = conn.cursor()

    c.execute("DELETE FROM TodoWorks WHERE oid=" + delete_box.get())
    conn.commit()
    conn.close()


def add_item():
    conn = sqlite3.connect('todolist.db')
    # making cursor
    c = conn.cursor()

    # instering into Table
    c.execute("INSERT INTO TodoWorks VALUES (:To_do)",
              {
                  'To_do': my_entry.get(),
              })

    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

    # comminting change
    conn.commit()

    # closing conn
    conn.close()


def query():
    conn = sqlite3.connect('todolist.db')
    # making cursor
    c = conn.cursor()

    c.execute("SELECT *,oid  FROM TodoWorks")
    records = c.fetchall()
    # print (records)

    print_records = ''
    for record in records:
        print_records += str(record[0]) + "  " + "\t" + str(record[1]) + "\n"

    query_label = Label(button_frame, text=print_records)
    query_label.grid(row=2, column=1)

    conn.commit()
    conn.close()


def cross_off_item():
    # Cross off Item
    my_list.itemconfig(
        my_list.curselection(),
        fg="#DEDEDE", )

    # Getting rid of selection bar
    my_list.select_clear(0, END)

    def uncross_item():
        # Cross off Item
        my_list.itemconfig(
            my_list.curselection(),
            fg="#464646", )

        # Getting rid of selection bar
        my_list.select_clear(0, END)

    def delete_crossed_item():
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#DEDEDE":
                my_list.delete(my_list.index(count))

            else:
                count += 1

        #  At list

    def save_list():
        file_name = filedialog.asksaveasfilename()
        initialdir = "Desktop",
        title = "Save File",
        filetypes = (
            ("Dat Files", ".dat"),
            ("All Files", ".* "))
        if file_name:
            if file_name.endswith(".dat"):
                pass
            else:
                file_name = f'{file_name}.dat'

                # Delete crossed off items before saving
            count = 0
            while count < my_list.size():
                if my_list.itemcget(count, "fg") == "#DEDEDE":
                    my_list.delete(my_list.index(count))

                else:
                    count += 1
            # GRABBING ALL FROM LIST
            stuff = my_list.get(0, END)

            # Open the file
            output_file = open(file_name, 'wb')
            # Add the stuff to the file
            pickle.dump(stuff, output_file)

    def open_list():
        file_name = filedialog.askopenfilename(
            initialdir="Desktop",
            title="Save File",
            filetypes=(
                ("Dat Files", ".dat"),
                ("All Files", ".* "))
        )

        if file_name:
            # Delete currently open list
            my_list.delete(0, END)

            # Open the file
            input_file = open(file_name, 'rb')

            # Load data from file
            stuff = pickle.load(input_file)

            # outputing Stuff on screen
            for item in stuff:
                my_list.insert(END, item)

    def delete_list():
        my_list.delete(0, END)

        # Create Menu

        # GUI Starting

    my_menu = Menu(root)
    root.config(menu=my_menu)
    # Add items to Menu
    file_menu = Menu(my_menu, tearoff=False)
    my_menu.add_cascade(label="File", menu=file_menu)

    # Add dropdown Items
    file_menu.add_command(label="Save List", command=save_list)
    file_menu.add_command(label="Open List", command=open_list)
    file_menu.add_separator()
    file_menu.add_command(label="Clear List", command=delete_list)

    # Adding buttons
    delete_button = Button(button_frame, text="Delete ITEM", command=delete_item)
    add_button = Button(button_frame, text="Add ITEM", command=add_item)
    cross_off_button = Button(button_frame, text="Cross_off ITEM", command=cross_off_item)
    uncross_button = Button(button_frame, text="Uncross ITEM", command=uncross_item)
    delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed_item)

    delete_button.grid(row=0, column=0)
    add_button.grid(row=0, column=1, padx=20, )
    cross_off_button.grid(row=0, column=2)
    uncross_button.grid(row=0, column=3, padx=20, )
    delete_crossed_button.grid(row=0, column=4)
    # CREATING QUERY BUTTON
    query_btn = Button(button_frame, text="SHOW RECORDS", command=query)
    query_btn.grid(row=1, column=2)
    # Delete from database
    delete_db_btn = Button(button_frame, text="Delete from db", command=delete_db)
    delete_db_btn.grid(row=1, column=3)

    delete_label = Label(button_frame, text="Delete ID")
    delete_box = Entry(button_frame, )

    delete_label.grid(row=4, column=2)
    delete_box.grid(row=4, column=3)

    # comminting change
    conn.commit()

    # closing conn
    conn.close()

    mainloop()