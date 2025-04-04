from tkinter import*
from datetime import date
 root = Tk()
 root.title('getting Started with Widgets')
 root.geometry('400x300')
 lbl = Label(text="Hey There!", fg="White", bg="#072F5F", height=1, width=300)
 name_lbl = label(text="Full Name ", bg="#3895D3")
 name_entry = Entry()
 def display():
        name = name_entry.get()
        global Message
        Message = "Welcome to the application!\nToday's date is:"
        greet = "hello"+name+"\n"
        text_box.insert(END,greet)
        text_box.insert(END, Message)
        text_bow.insert(END,date.today())
 text_box = text(heights=3)
 btn = Button(text="begin", command=display, height=1, bg="#1261A0",fg='white')
 lbl.pack()
 name_lbl.pack()
 name_entry.pack()
 btn.pack()
 text_box.pack()