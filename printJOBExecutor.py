from tkinter import *
from tkinter import messagebox
from functionsFile import *
from threading import Thread
import time
import pythoncom
pythoncom.CoInitialize()
schedule.every(120).seconds.do(mass_job)
master = Tk()
master.title("printJOB (Alpha) Client")
variable = StringVar(master)
def checkQueue():
    schedule.Job.do(mass_job)
    time.sleep(2)
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
master.geometry('500x100')
master.resizable(False, False)
mainloop()






