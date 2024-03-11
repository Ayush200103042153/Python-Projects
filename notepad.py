from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("600x600")
root.title("Notepad")
root.config(bg='lightblue')
root.resizable(False,False)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text files','*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(INSERT,content)

b1=Button(root,width='20',height='2',bg='white',text='Save File',command=save_file).place(x=100,y=5)
b2=Button(root,width='20',height='2',bg='white',text='Open File',command=open_file).place(x=300,y=5)

entry=Text(root,width='72',height='33',wrap=WORD).place(x=10,y=60)

root.mainloop()