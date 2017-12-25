# -*- coding: utf-8 -*-

import Tkinter
from PIL import ImageTk
import qrcode

def qrmake(qrstr):
	global n
	n = n + 1
	print qrstr
	qr=qrcode.QRCode(version=19, box_size=3, border=2)
	qr.add_data(qrstr)
	qr.make(fit=True)
	img=qr.make_image()
	img.save('qrcode.png')
	bm.append(ImageTk.PhotoImage(file = 'qrcode.png'))
	label.configure(image = bm[n])
	setCenter()
	
def submit():
	global i, data
	data = ent.get("0.0", "end")
	i = -1
	nextpic()

def nextpic():
	global i, data
	i = i + 1
	qrlen = 300
	qrmake(data[qrlen*i:qrlen*(i+1)])

def setCenter():
	top.update_idletasks()
	x = (top.winfo_screenwidth()  - top.winfo_reqwidth())/2
	y = (top.winfo_screenheight() - top.winfo_reqheight())/2
	top.geometry("+%d+%d"%(x,y))

top = Tkinter.Tk()

n = -1
bm = []

label = Tkinter.Label(top)
ent  = Tkinter.Text(top, width = 36, height = 5)
btn1 = Tkinter.Button(top, text = 'Set',  command = submit)
btn2 = Tkinter.Button(top, text = 'Next', command = nextpic)

label.pack()
ent.pack()
btn1.pack()
btn2.pack()

qrmake('hello, qrc')

top.mainloop()
