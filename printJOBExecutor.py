from tkinter import *
from functionsFile import *
from threading import Thread
import time
import pythoncom
pythoncom.CoInitialize()
schedule.every(150).seconds.do(mass_job)
master = Tk()
master.title("printJOB (Alpha) Client")
variable = StringVar(master)
def closeWindow():
    #schedule.run_all() #ToDo fix it
    time.sleep(2)
    return
thread = Thread(target = run_schedule)
thread.start()
button1= Button(master, text="Çap yoxla", command=closeWindow)
button1.pack()
def shut():
    master.destroy()
    return
button2=Button(master,text='Baqla',command=shut)
button2.pack()
text = Text(master)
text.insert(INSERT, "Proqramı bağlamaq üçün 'Bağla' tıklayın \nBaş osifdən çap növbəsin yoxlamaq üçün 'Çapı yoxla' tıklayın")
text.place(x=10,y=30)
text.pack()
master.geometry('500x100')
master.resizable(False, False)
mainloop()






