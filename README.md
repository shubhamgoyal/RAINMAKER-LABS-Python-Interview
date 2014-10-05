This repository is created as an answer to the first question for a web developer position at RAINMAKER LABS.

Here is the question -
You are given an HTML form, which contains the following entries:
<input type="checkbox" class="form" name="checkbox_2"/> 
<input type="checkbox" class="form" name="checkbox_1"/> 
<input type="checkbox" class="form" name="checkbox_3"/> 
... 
<input type="checkbox" class="form" name="checkbox_10"/> 
The above form has been submitted using the "POST" method.
Write code that will determine which checkboxes have been checked and print, in a space separated list, the checkbox numbers that were checked.
For example, if check-boxes 3, 5, and 10 are checked, you would print
3 5 10

I assumed that the framwork being used in the web project was Flask. I created a simple Flask backend just to process the data in the POST request and print the checkbox numbers. My very simple barebone HTML template file (app/templates/form_submit.html) attempts to re-create the scenario in the question by creating a form that has 10 checkboxes and one 'Submit' button. My backend logic file (app/views.py) contains the required code to parse the POST request and print the checkbox numbers.