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
w_momentum = 0
b_momentum = 0
momentum = 0.9
while(i<5000):
	error = 0
	w_gradient = 0
	b_gradient = 0
	f = w * x + b
	error = error + 0.5*dot((f - y),(f - y))
	#newtown
	w_gradient = w_gradient + dot((f - y),x) 
	b_gradient = b_gradient + sum(f - y) 
	print "epoch:%d,error:%f\n" % (i,error)
	w_momentum = momentum * w_momentum + (1-momentum) * w_gradient
	b_momentum = momentum * b_momentum + (1-momentum) * b_gradient
	w = w - w_momentum * step
	b = b - b_momentum * 2 * step
	if(i%500==0):
		plt.plot(x,y,'*') #data point
		plt.plot(x_plot,w*x_plot+b,'r-') #prediction
		plt.show()
	i = i+1
print "w:%f\nb:%f" %(w,b)	

