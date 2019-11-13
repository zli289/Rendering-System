import MatrixCaculation as M
import Texture

class SingleObject(object):
	def __init__(self, Points, Polygons,location,numofPolygon):
		self.Polygons=Polygons
		self.numofPolygon=numofPolygon	

		self.Points= self.LocaltoWorld(Points,location)
		self.scrPoints=[]
		self.devPoints=[]

		self.color=[20,240,240]
		self.texture=Texture.cylind(self.Points)

		self.normals= self.getnormals()
		self.v_normals=self.getVertexNormals()

	def LocaltoWorld(self,Points,location):
		for i in Points:
			for j in range(3):
				i[j]+=location[j]
		return Points

	def WorldtoScreen(self,c):
		matrix=c.Matrix()
		for i in self.Points:		
			self.scrPoints.append(M.pointmul(matrix,i))
		return self.scrPoints

	def ScreentoDevices(self):
		for i in self.scrPoints:
			x=i[0]/i[3]
			y=i[1]/i[3]
			result=1
			while x*result>1 or y*result>1 or x*result<-1 or y*result< -1:
				result /=10
		for i in self.scrPoints:
			self.devPoints.append([i[0]/i[3]*result*1000+500,i[1]/i[3]*result*1000+400,i[2]/i[3]*result*1000])
		return self.devPoints

	def getnormals(self):
		normals=[]
		for polygon in self.Polygons:		
			p1=self.Points[polygon[3]-1]
			p2=self.Points[polygon[1]-1]
			p3=self.Points[polygon[2]-1]			

			v1=M.subtract(p2,p1)
			v2=M.subtract(p3,p2)

			normal=M.crossproduct(v1,v2)
			normals.append(normal)
		return normals

	def backfaceculling(self,c):
		for i in range(self.numofPolygon-1,-1,-1):
			p1=self.Points[self.Polygons[i][2]-1]
			n0=M.subtract(c.c,p1)
			if M.dotproduct(self.normals[i],n0)>=0:
				del self.Polygons[i]
				del self.normals[i]

	def getVertexNormals(self):
		#get around normals of Polygons
		v_normals=[[0,0,0] for i in range(len(self.Points))]

		for index in range(self.numofPolygon):
			for vertex in self.Polygons[index][1:]:
		#		for i,point in enumerate(self.Points):
		#			if self.Points[vertex-1]==point:
		#				v_normals[i]=M.add(v_normals[i],self.normals[index])
				v_normals[vertex-1]=M.add(v_normals[vertex-1],self.normals[index])
			
		for index in range(len(v_normals)):
			v_normals[index]=M.normalize(v_normals[index])

		return v_normals
