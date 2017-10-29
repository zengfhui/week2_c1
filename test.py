#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
#from flask import Flask 
#from flask import render_template
import os
import json

#print(os.getcwd())
path = '/home/shiyanlou/files'
s = os.listdir('/home/shiyanlou/files')

f_path = '/home/shiyanlou/files'
filename_list = os.listdir('/home/shiyanlou/files')


file_dict = {}


for filename in filename_list:
	with open(f_path + '/' + filename) as file:
		 file_dict[filename] = json.load(file)

def dict_operation(file_dict):
	data = {}
	for key,value in file_dict.items():
		key = key.encode()
		value = value.encode()
		data[key] = value
	data['content'] = data['content'].split(' \\n ')

	return data

#a = filename_list[1]
#print(dict_operation(file_dict[a]))
#d = dict_operation(file_dict[a])
#for line in d['content']:
#	print(line)


a ={1:1}
b ={2:2}
c ={3:3}
s ={'a':a,'b':b}
print(s['a'][1])
