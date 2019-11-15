import tkinter

def toRGB(texture,intensity):
	rgb='#'
	for i in range(3):
		num=abs(int(texture[i]*intensity[i]))
		r=str(hex(num))[2:]
		if len(r)==1:
			r='0'+r
		rgb+=r
	return rgb

def drawing(singleobject):
	root = tkinter.Tk()
	canvas = tkinter.Canvas(root,bg='white',height=800,width=1000)
	canvas.pack()
	points=singleobject.devPoints
	for polygon in singleobject.Polygons:
		onepolygon=[]
		for j in polygon[1:]:
			vertex=j-1
			onepolygon.extend([points[vertex][0],points[vertex][1]])
		onepolygon.extend([onepolygon[0],onepolygon[1]])
		canvas.create_line(onepolygon,width=1)
	root.mainloop()

def renderforscan(results,intensities):
	root = tkinter.Tk()
	canvas = tkinter.Canvas(root,bg='white',height=800,width=1000)
	canvas.pack()
	for polygon in results:
		color=toRGB([],intensities.pop(0))
		for line in polygon:
			l=[]
			y=line.pop(0)
			for x in line:
				l.extend([x[0],y])
			canvas.create_line(l,width=1,fill=color)
	root.mainloop()

def renderforpixel(i_buffer,t_buffer):
	root = tkinter.Tk()
	canvas = tkinter.Canvas(root,bg='white',height=800,width=1000)
	canvas.pack()
	for y_index,y in enumerate(i_buffer):
		for x_index,intensity in enumerate(y):
			if intensity!=-1:
				canvas.create_line(x_index,y_index,x_index+1,y_index,width=1,fill=toRGB(t_buffer[y_index][x_index],intensity))
	root.mainloop()

def noiseimage(noise,H,W):
	root = tkinter.Tk()
	canvas = tkinter.Canvas(root,bg='white',height=800,width=1000)
	canvas.pack()
	x=0
	y=0
	z_x = 0.05
	z_y = 0.05
	for i in range(H):
		for j in range(W):
			canvas.create_line([j+200,i+200,j+201,i+200],width=1,fill=toRGB(noise[i][j],[1,1,1]))
			x+=z_x
		y+=z_y
		x=0.0
	root.mainloop()
