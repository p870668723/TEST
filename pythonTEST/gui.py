# -*- coding:utf-8 -*- 
import tkinter.messagebox as messagebox
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        #self.helloLable = Label(self, text='f')
        #self.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text= 'Hello', command=self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self, text= 'QUIT',command=self.quit)
        self.quitButton.pack({'side':'left'})
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('MESSAGE', 'Hello, %s'%name)

app =Application()
app.master.title('DEMO')
app.mainloop()
