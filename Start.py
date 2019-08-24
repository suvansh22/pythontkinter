from Tkinter import *
splash=Tk()
img=PhotoImage(file='car.gif')
def fun(e=0):
    splash.destroy()
    import project
lb=Label(splash,image=img,font='24000',fg='orange')
lb.pack()
Label(splash,text='SUVANSH AGRAWAL',font='200').pack()
Label(splash,text='171B139',font='200').pack()
Label(splash,text='9425308654',font='200').pack()
lb.bind('<Motion>',fun)
splash.mainloop()
