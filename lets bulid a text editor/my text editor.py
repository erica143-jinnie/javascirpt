from tkinter import*
from tkinter.filedialog import askopenfile, asksaveasfilename

window = Tk()
window.title("codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
            filetypes=[("Text files",*.txt"),("All flies","*.*)]
            )
            if not filepath:
                    return
            txt_edit.delete(1.0,END)
            with open(filepath,"r")as input_file:
            text = input_file.read()
        