#!/bin/python

from flask import Flask
from flask import request

defaults = ''

app = Flask(__name__)

@app.route('/')
def my_form():
        template = '<head><meta name="viewport" content="width=device-width"></head><form action="." method="POST"><textarea id="text" name="text" cols="60" rows="10">' + defaults + '</textarea><br><input type="submit" name="my-form" value="Upload Text"></form>'
	return template

@app.route('/', methods=['POST'])
def my_form_post():
	global defaults
        defaults = format(request.form['text'])
	print defaults
        template = '<head><meta name="viewport" content="width=device-width"></head><form action="." method="POST"><textarea id="text" name="text" cols="60" rows="10">' + defaults + '</textarea><br><input type="submit" name="my-form" value="Upload Text">Text was uploaded successfully!</form>'
	return template

if __name__ == '__main__':
        app.run(threaded=True, debug=True, host='0.0.0.0', port=6664)
