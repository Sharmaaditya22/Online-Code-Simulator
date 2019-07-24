#!/usr/bin/python
#from __future__ import printfunction
import cgi, cgitb
import os
import json
cgitb.enable()
#print("Content-type: application/json")
#print()
form = cgi.FieldStorage()

a=form.getvalue('lang')
b=form.getvalue('data')
try:
	if(a=="py"):
		f=open("firstpy.py","w")
		f.write(b)
		f.flush()
		f.close
		os.system("python3 firstpy.py &> output.txt")
	else:
		f=open("firstc.c","w")
		f.write(b)
		f.flush()
		f.close
		os.system("python3 pythonC.py &> output.txt")
		
	f = open("output.txt", "r")
	file = f.read()
	#f.flush()
	f.close()

	x = {
		"code_output": file
	}
	f = open('log.txt', 'a')
	f.write('dump up')
	f.close()
	j=json.dumps(x,ensure_ascii=False)

	print "Content-type:application/json\r\n\r\n"
	print j

except:
	f=open("output.txt","w")
	f.write("can't run file")
	f.close


