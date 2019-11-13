import math 
import math
import random
import tkinter
def cylind(Points):
	zs= [Points[i][2] for i in range(len(Points))]
	h=max(zs)-min(zs)
	uv=[]
	for point in Points:
		r=math.sqrt(point[0]**2+point[1]**2)

		z=point[2]
		if z>=0:
			z+=h/2
		elif z<0:
			z=h/2-abs(z)
		z/=h

		if r==0:
			b=0
		else:
			b=math.acos(abs(point[0])/r)
		if point[1]>=0:
			if point[0]<0:
				b=math.pi-b
		elif point[1]<0:
			if point[0]>=0:
				b=2*math.pi-b
			elif point[0]<0:
				b=math.pi+b

		uv.append([b/(2*math.pi),z])
	return uv

W = 600
H = 400

def datatable(H,W):
	data = [[0,0] for i in range(W*H)]
	num = random.Random()
	for i in range(H):
	    for j in range(W):
	    	x = float((num.randint(1,2*W))-W)/W
	    	y = float((num.randint(1,2*H))-H)/H
	    	s = math.sqrt(x*x+y*y)
	    	if s!=0:
	    	    x = x / s
	    	    y = y / s
	    	else:
	    		x = 0
	    		y = 0
	    	data[i*H+j] = (x,y)
	return data

def dotproduct(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]

def noise(x,y,data):
    x1 = math.floor(x)
    y1 = math.floor(y)
    x2 = x1+1
    y2 = y1+1

    s = dotproduct(data[int(x1)+int(y1)*H],(x-x1, y-y1))
    t = dotproduct(data[int(x2)+int(y1)*H],(x-x2, y-y1))
    u = dotproduct(data[int(x1)+int(y2)*H],(x-x1, y-y2))
    v = dotproduct(data[int(x2)+int(y2)*H],(x-x2, y-y2))

    s_x = (x-x1)**2*3-(x-x1)**3*2
    a = s + s_x*t - s_x*s
    b = u + s_x*v - s_x*u

    s_y = (y-y1)**2*3-(y-y1)**3*2
    z = a + s_y*b - s_y*a
    return z

def textureimage(H,W):
	data=datatable(H,W)   
	image=[]
	x=0
	y=0
	z_x = 0.05
	z_y = 0.05
	for i in range(H):
		row=[]
		for j in range(W):
			color = [round((255-(255*noise(x,y,data)))) for i in range(3)]
			row.append(color)
			x+=z_x
		y+=z_y
		x=0.0
		image.append(row)
	return image

