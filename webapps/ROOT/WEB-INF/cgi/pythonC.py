#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:15:29 2018

@author: adityasharma
"""

import os
try:

	os.system("gcc -o ts firstc.c")
	os.system("./ts")
except:
	f=open("output2.txt","w")
	f.write("can't open C file")
	f.close
    