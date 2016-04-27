from sys import argv
from os.path import exists
s,inn,outn = argv
in_file = open(inn,'r+')
out_file = open(outn,'w+')
a = in_file.read()
print "%r" % exists(outn)
out_file.write(a)
print out_file.read()
out_file.close()
in_file.close()
