import MatrixCaculation as M
# Define the camera and View Transformation martrixes
class Camera(object):
	def __init__(self,c,p_ref,d,h,f):
		self.c=c
		self.p_ref=p_ref
		self.d=d
		self.h=h
		self.f=f
		self.v1=[0,-1,0]

		self.N=M.normalize(M.subtract(self.p_ref,self.c))
		self.U=M.normalize(M.crossproduct(self.N,self.v1))
		self.V=M.crossproduct(self.U,self.N)

	def Matrix(self):
		rotation=[
			[self.U[0],self.U[1],self.U[2],0],
			[self.V[0],self.V[1],self.V[2],0],
			[self.N[0],self.N[1],self.N[2],0],
			[0,0,0,1]]
		t=[
			[1,0,0,-self.c[0]],
			[0,1,0,-self.c[1]],
			[0,0,1,-self.c[2]],
			[0,0,0,1]]
			
		View=M.matmul(rotation,t)

		Pers=[
			[self.d/self.h,0,0,0],
			[0,self.d/self.h,0,0],
			[0,0,self.f/(self.f-self.d),-(self.d*self.f)/(self.f-self.d)],
			[0,0,1,0]]

		return M.matmul(Pers,View)