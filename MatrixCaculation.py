import math

# Point multiple Matrix
def pointmul(m,p):
	result=[0,0,0,0]
	for i in range(4):
		for j in range(4):
			result[i]+=m[i][j]*p[j]	
	return result 

# Vectors Multiplation
def crossproduct(a,b):
	return [(a[1]*b[2]-a[2]*b[1]),(a[2]*b[0]-a[0]*b[2]),(a[0]*b[1]-a[1]*b[0])]

def subtract(a,b):
	return [a[0]-b[0],a[1]-b[1],a[2]-b[2]]

def add(a,b):
	return [a[0]+b[0],a[1]+b[1],a[2]+b[2]]

def dotproduct(a,b):
	sum=0
	for i in range(3):
		sum+=a[i]*b[i]
	return sum

def multiple(a,b):
	return [a[0]*b,a[1]*b,a[2]*b]

# Matrix Multiplation
def matmul(m1,m2):
	result=[[0]*4 for row in range(4)]
	for i in range(4):
		for j in range(4):
			for k in range(4):
				result[i][j]+=m1[i][k]*m2[k][j]
	return result

# Computing N, V vectors
def normalize(x):
	result=0
	for i in x:
		result+=i*i
	result=math.sqrt(result)
	if result!=0:
		return [x[0]/result,x[1]/result,x[2]/result]
	else:
		return x

