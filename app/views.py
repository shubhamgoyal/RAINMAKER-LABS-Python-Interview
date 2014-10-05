from app import app
from flask import render_template, request
import re
import sys

@app.route('/')
def form():
    return render_template('form_submit.html')

@app.route('/', methods=['POST'])
def handle_form_submit():
	for input_element in request.form:
		if input_element.startswith('checkbox_'):
			print(re.findall('\d+', input_element)[0], end=" ")
	print()
	return "See the console for a list of checkbox numbers that were checked"