from sys import argv
s,filename = argv
txt = open(filename,'w+')
print txt.read()
txt.truncate()
txt.write('I\'m handsome again')
print txt.read()

