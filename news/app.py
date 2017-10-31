#!/usr/bin/env python3

import flask
from flask import Flask,render_template
import os
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

class Files():
	def __init__(self):
		self.path = '/home/shiyanlou/files'
		self.filename_list = self._get_filename_in_files()
		self.file_dict = self._read_all_files()


	def _read_all_files(self):
		file_dict = {}
		f_path = '/home/shiyanlou/files'
		for filename in self.filename_list:
			with open(f_path + '/' + filename) as file:
				 file_dict[filename[:-5]] = json.load(file)	#[:-5],get rid of '.json'
		return file_dict

#		for filename in self.filename_list:
#			for key,value in file_dict[filename].items():
#				key = key.encode()
#				value = value.encode()

#	a = filename_list[0]
#	print(dict_operation(file_dict[a]))
#	a ={1:1}
#	b ={2:2}
#	c ={3:3}
#	s ={'a':a,'b':b}
#	print(s['a'][1])


	def _get_filename_in_files(self):
		
		s = os.listdir('/home/shiyanlou/files')
		f_path = '/home/shiyanlou/files'
		filename_list = os.listdir('/home/shiyanlou/files')
		return filename_list

	def get_filename_list(self):
		return self.filename_list

	def get_file_by_filename(self,filename):
		return self.file_dict[filename]


files = Files()

@app.route('/')
def index():
	filename_list = files.get_filename_list()
	return render_template('index.html',filename_list=filename_list )

@app.route('/files/<filename>')
def file(filename):
	if filename in files.file_dict:
		_file = files.get_file_by_filename(filename)
		return render_template('file.html',_file=_file)
	else:
		return render_template('404.html'),404	

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'),404


if __name__ == '__main__':
	app.run()

		