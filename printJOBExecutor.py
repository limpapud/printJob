from tkinter import *
from tkinter import messagebox
from functionsFile import *
from threading import Thread
import time
import pythoncom
pythoncom.CoInitialize()
master = Tk()
master.title("printJOB (Alpha) Client")
master.geometry('500x100')
master.resizable(False, False)
variable = StringVar(master)
checkInBranch()
def checkQueue():
    mass_job()
    return
thread = Thread(target = run_schedule)
thread.start()
button1= Button(master, text="Çap yoxla", command=checkQueue)
button1.pack()
def closeWindow():
    if messagebox.askokcancel("Çıxış", "Çıxış etmək istədiyinzə əminsiniz mi?"):
        master.destroy()
        #ToDo thread is not dying while exiting. TB Fixed
master.protocol("WM_DELETE_WINDOW", closeWindow)
text = Text(master)
text.insert(INSERT, "Proqramı bağlamaq üçün 'Bağla' tıklayın \nBaş osifdən çap növbəsin yoxlamaq üçün 'Çapı yoxla' tıklayın")
text.place(x=10,y=30)
text.pack()

mainloop()






