import MatrixCaculation as M
import Rendering
import Interpolation
from PIL import Image
import numpy as np
import Texture
def illuminate(normal,camera,light,i_light,ks,ka,kd):
	#calculate R\
	n=1
	h=M.normalize(M.add(light,camera))
	#normal1=M.normalize(normal)
	i_s=M.multiple(i_light,M.dotproduct(normal,h)**n*ks)
	#i_a=M.multiple(i_light,ka)
	#i_d=M.multiple(light1,M.dotproduct(normal,light1)*kd)

	return i_s

def Constant(object1):
	#	polygon's intensities
	intensities=[]
	for normal in object1.normals:
		intensities.append(illuminate(M.normalize(normal),c_pos,light,i_light,ks,ka,kd))
	#	inerpolation
	results=Interpolation.ScanConversion(object1)
	#	rendering
	Rendering.objectcolor=object1.color
	Rendering.renderforscan(results,intensities)

def Ground(object1):
	#data=Texture.textureimage()
	image= Image.open('stripe.jpg')
	data=np.asarray(image)
	#	vertex's intensites
	v_intensities=[]
	for v_normal in object1.v_normals:
		v_intensities.append(illuminate(v_normal,c_pos,light,i_light,ks,ka,kd))
	object1.v_normals=v_intensities
	#	interpolate intensities
	results=Interpolation.ScanConversion(object1)
	i_buffer,t_buffer=Interpolation.Z_buffer(results)
	#	illmination
	for y_index,y in enumerate(i_buffer):
		for x_index,color1 in enumerate(y):
			if color1!=-1:
				t_buffer[y_index][x_index]=object1.color
	#	rendering
	Rendering.renderforpixel(i_buffer,t_buffer)

def Phong(object1):
	#data=Texture.textureimage()
	image= Image.open('stripe.jpg')
	data=np.asarray(image)
	#	interpolate vertex's normals
	results=Interpolation.ScanConversion(object1)
	i_buffer,t_buffer=Interpolation.Z_buffer(results)
	#	illmination
	for y_index,y in enumerate(i_buffer):
		for x_index,color1 in enumerate(y):
			if color1!=-1:
				i_buffer[y_index][x_index]=illuminate(color1,c_pos,light,i_light,ks,ka,kd)
				pos=t_buffer[y_index][x_index]
				t_buffer[y_index][x_index]=data[int(pos[0]*400-1)][int(pos[1]*600-1)]
	#	rendering
	Rendering.renderforpixel(i_buffer,t_buffer)

def textureimage(H,W):
	data=Texture.textureimage(H,W)
	Rendering.noiseimage(data,H,W)