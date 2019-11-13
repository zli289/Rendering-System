import re
# Get Points and Polyons
def readfile(filename):
	file=open(filename,'r')
	data=re.split(r'\n',file.read())
	
	nums=re.findall(r'\S+',data.pop(0))
	numofPoints=int(nums[1])
	numofPolygon=int(nums[2])

	Points=[[1.0]*4 for i in range(numofPoints)]
	for i in range(numofPoints):
		point= re.findall(r'\S+',data.pop(0))
		Points[i][:3]=[float(x) for x in point]

	Polygons=[]
	for i in range(numofPolygon):
		polygon=re.findall(r'\S+',data.pop(0))
		Polygons.append([int(x) for x in polygon])

	return Points, Polygons, numofPolygon
