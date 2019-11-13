import MatrixCaculation as M
import sys

class Edge(object):
	def __init__(self,ymin,ymax,x_ymin,z_ymin,z_ymax,m,vnor_ymin,vnor_ymax,t_ymin,t_ymax):
		self.ymin=ymin
		self.ymax=ymax
		#	z-buffer
		self.x_ymin=x_ymin
		self.m=m

		self.z_ymin=z_ymin
		self.z_ymax=z_ymax
		self.z=z_ymin
		#	vertex's normal
		self.vnor_ymin=vnor_ymin
		self.vnor_ymax=vnor_ymax
		self.v_normal=vnor_ymin
		#	texture
		self.t_ymin=t_ymin
		self.t_ymax=t_ymax
		self.t=t_ymin

def ScanConversion(singleobject):
	results=[]
	for polygon in singleobject.Polygons:
		result=[]
		edges=[]
		num=polygon.pop(0)
		for i in range(num-1):
			edges.append([polygon[i]-1,polygon[i+1]-1])
		edges.append([polygon[num-1]-1,polygon[0]-1])
		y=sys.maxsize
		edgetable=[]
		for edge in edges:
			start=singleobject.devPoints[edge[0]]
			end=singleobject.devPoints[edge[1]]
			#	vertex normals
			start.append(singleobject.v_normals[edge[0]])
			end.append(singleobject.v_normals[edge[1]])
			#	vertex texture
			start.append(singleobject.texture[edge[0]])
			end.append(singleobject.texture[edge[1]])
			#horizon line doesn't count
			if start[1]==end[1]:
			 	continue
			if start[1] > end[1]:
				start, end= end, start
			#computing k 
			if end[0]==start[0]:
				m=0
			else:
				m=(end[1]-start[1])/(end[0]-start[0])
			#shorten one y_max
			edgetable.append(Edge(start[1],end[1]-1,start[0],start[2],end[2],m,start[3],end[3],start[4],end[4]))
			y=min(start[1],y)

		#initialize et & y
		ate=[]
		y=int(y)
		while ate or edgetable:
			for i in range(len(edgetable)-1,-1,-1):
				if edgetable[i].ymin <y:
					ate.append(edgetable[i])
					del edgetable[i]
			ate=sorted(ate,key= lambda x:x.x_ymin)
			# 3.2 Fill in desired pixel values on scan line y by using pairs of x coordinates from the AET 
			intersects=[]
			for edge in ate:
				if edge.x_ymin not in [i[0] for i in intersects]:
					intersects.append([edge.x_ymin,edge.z,edge.v_normal,edge.t])
			# single y line format: [y, [x1,z1],[x2,z2]]
			if len(intersects)>1:
				intersects.insert(0,y)
				result.append(intersects)	

			for i in range(len(ate)-1,-1,-1):
				if ate[i].ymax<y:
					del ate[i]
				elif ate[i].m!=0:
					ate[i].x_ymin+=1/ate[i].m 	
					
					y1=ate[i].ymax
					y2=ate[i].ymin

					z1=ate[i].z_ymax
					z2=ate[i].z_ymin
						
					l1=ate[i].vnor_ymax
					l2=ate[i].vnor_ymin

					t1=ate[i].t_ymax
					t2=ate[i].t_ymin

					ate[i].z+=(z1-z2)/(y1-y2)
					ate[i].v_normal=M.add(M.multiple(l1,(y-y2)/(y1-y2)),M.multiple(l2,(y1-y)/(y1-y2)))
					ate[i].t=[(t1[0]*(y-y2)+t2[0]*(y1-y))/(y1-y2),(t1[1]*(y-y2)+t2[1]*(y1-y))/(y1-y2)]

				# 3.6 Increment y by 1 (to the coordinate of the next scan line)
			y+=1				
		results.append(result)
	return results

def Z_buffer(Polygons):
	z_buffer=[[sys.maxsize]*1200 for i in range(1000)]
	i_buffer=[[-1]*1200 for i in range(1000)]
	t_buffer=[[-1]*1200 for i in range(1000)]
	for onepolygon in Polygons:
		for line in onepolygon:
			y=line.pop(0)		
			start=line[0]
			end=line[len(line)-1]

			xa=start[0] 
			xb=end[0]
			
			za=start[1]
			zb=end[1]

			la=start[2]
			lb=end[2]

			ta=start[3]
			tb=end[3]

			xp=xa
			zp=za
			while xp<xb:
			# For every x in y get z
				zp+=(zb-za)/(xb-xa)
				# Visible
				if zp< z_buffer[y][int(xp)]:
					z_buffer[y][int(xp)]=zp
					i_buffer[y][int(xp)]=M.add(M.multiple(la,(xb-xp)/(xb-xa)),M.multiple(lb,(xp-xa)/(xb-xa)))
					t_buffer[y][int(xp)]=[(ta[0]*(xb-xp)+tb[0]*(xp-xa))/(xb-xa),(ta[1]*(xb-xp)+tb[1]*(xp-xa))/(xb-xa)]
				xp+=1

	return i_buffer,t_buffer


