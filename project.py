from Tkinter import *

master = Tk()
def call():
	sure.config(relief=SUNKEN)
	n_sure.config(relief=RAISED)
	
def call2():
	sure.config(relief=RAISED)
	n_sure.config(relief=SUNKEN, bg='Dark Green', activebackground='red')
def call3():
	sure.config(relief=RAISED)
	n_sure.config(relief=RAISED)

f = Frame(master, height=100, width=100)#notice frame
f.pack(padx = 100 ,pady = 100)

sure = Button(f, text="Sure!", command=call)
n_sure = Button(f, text="Not Sure!", command=call2)

sure.pack(fill=BOTH, expand=0)
n_sure.pack(fill=BOTH, expand=0)

d = Button(f, text="DISABLED Button", state=DISABLED)
g = Button(f, text='reset', command=call3)
d.pack()
g.pack()


w = Canvas(master, width=200, height=100)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")


mainloop()