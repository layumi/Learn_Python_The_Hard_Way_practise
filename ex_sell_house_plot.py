import matplotlib.pyplot as plt
from numpy import *
x = array([0.2104,0.1600,0.2400,0.1416,0.3000])
y = array([0.400,0.330,0.369,0.232,0.540])
s = size(x)
w = 0
b = 0
one = array([1]*s)
x_plot = arange(100)*0.003+0.1
i = 0
step = 0.1
while(i<5000):
	error = 0
	w_gradient = 0
	b_gradient = 0
	f = w * x + b
	error = error + 0.5*dot((f - y),(f - y))
	w_gradient = w_gradient + dot((f - y),x)
	b_gradient = b_gradient + dot(f - y,one)
	print "epoch:%d,error:%f\n" % (i,error)
	#print w_gradient
	#print b_gradient
	w = w - step*w_gradient
	b = b - 2*step*b_gradient
	if(i%500==0):
		plt.plot(x,y,'*') #data point
		plt.plot(x_plot,w*x_plot+b,'r-') #prediction
		plt.show()
	i = i+1
print "w:%f\nb:%f" %(w,b)	

