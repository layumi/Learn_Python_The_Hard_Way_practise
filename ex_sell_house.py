x = [0.2104,0.1600,0.2400,0.1416,0.3000]
y = [0.400,0.330,0.369,0.232,0.540]
w = 1.58
b = 0.04
i = 0
step = 0.1
while(i<10000):
	j = 0 
	error = 0
	w_gradient = 0
	b_gradient = 0
	while (j<5):
		f = w * x[j] + b
		error = error + 0.5*(f - y[j])*(f - y[j])
		w_gradient = w_gradient + (f - y[j])*x[j]
		b_gradient = b_gradient + f - y[j]
		j = j+1
	print "epoch:%d,error:%f\n" % (i,error)
	#print w_gradient
	#print b_gradient
	w = w - step*w_gradient/5
	b = b - 2*step*b_gradient/5
	i = i+1
print "w:%f\nb:%f" %(w,b)
	

