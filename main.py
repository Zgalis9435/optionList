import tkinter
from tkinter import *

appList=Tk()
list=['Python','Java','JavaScript','React']
castList=tkinter.StringVar(value=list)
etiqueta=Label(text='Lenguajes de programación')
boxList=tkinter.Listbox(appList,height=5,listvariable=castList)
boxList.pack()
etiqueta.pack()

appList.mainloop()
