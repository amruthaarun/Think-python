from swampy.Gui import *

def call2():
	g.la(text='GUI PROGRAMMING')

def call1():
	g.bu(text='press here again', command=call2)

g=Gui()
g.title('Gui')

button1=g.bu(text='press here', command=call1)
g.mainloop()

