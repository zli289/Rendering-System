import Camera
import SingleObject
import Readfile 
import Shading
#	Loading file
Points1,Polygons1, numofPolygon1=Readfile.readfile('D files/better-ball.d.txt')
#	Camera configuration
c_pos=[5,5,10]
p_ref=[0,0,0]
d=20
h=15
f=80
c=Camera.Camera(c_pos,p_ref,d,h,f)
#	Object initialization
object1=SingleObject.SingleObject(Points1,Polygons1,[0,0,0],numofPolygon1)
object1.backfaceculling(c)
object1.WorldtoScreen(c)
object1.ScreentoDevices()
#	Object's color(RGB)
object1.color=[20,200,160]
Shading.Rendering.color=object1.color
#	Light source configuration
Shading.light=[30,30,30]
Shading.i_light=[0.8,0.8,0.8]
Shading.ka=0.4
Shading.ks=1
Shading.kd=0.6
Shading.c_pos=c_pos
# choose rendering

rendering=2
if rendering==1:
	Shading.Rendering.drawing(object1)
elif rendering==2:
	Shading.Constant(object1)
elif rendering==3:
	Shading.Ground(object1)
elif rendering==4:
	Shading.Phong(object1)
elif rendering==5:
	Shading.AddTexture(object1)
elif rendering==6:
	Shading.textureimage(256,256)
