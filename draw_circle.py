from swampy.Gui import *
g=Gui()
def draw_circle(fill_color='black'):
	canvas=g.ca(width=300, height=300,bg='white')
	c=canvas.circle([0,0],100,outline='black')
	c.config(fill=fill_color)
def read():
	color=ent.get()
	print color
	colors=['white','black','red','green','blue','cyan','yellow','magenta']
	for c in colors:
		print c
		if color == c:
			draw_circle(color)
			return
	print "no color match"
	
	
g.bu(text='Draw circle', command=draw_circle)
g.title('draw cicle')
ent=g.en()
g.bu(text='second button',command=read)
g.mainloop()
