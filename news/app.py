#!/usr/bin/env python3

from flask import Flask,render_template
import os
import json

app = Flask(__name__)

def dict_operation(file_dict):
	data = {}
	for key,value in file_dict.items():
		key = key.encode()
		value = value.encode()
		data[key] = value
	data['content'] = data['content'].split(' \\\\n ')

	return data

@app.route('/')
def index():
		
	path = '/home/shiyanlou/files'
	s = os.listdir('/home/shiyanlou/files')

	f_path = '/home/shiyanlou/files'
	filename_list = os.listdir('/home/shiyanlou/files')

	file_dict = {}

	for filename in filename_list:
		with open(f_path + '/' + filename) as file:
			 file_dict[filename] = json.load(file)

	return render_template('index.html',file_dict)

#	a = filename_list[0]
#	print(dict_operation(file_dict[a]))
#	a ={1:1}
#	b ={2:2}
#	c ={3:3}
#	s ={'a':a,'b':b}
#	print(s['a'][1])







@app.route('/files/<filename>')
def file(filename):
	pass




@app.errorhandler
def not_found(error):
	return render_template('404.html',404)