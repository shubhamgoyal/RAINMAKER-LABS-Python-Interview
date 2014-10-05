This repository is created to store my solutions for the Python interview questions for a web developer position at RAINMAKER LABS.

Question 1 -
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

Answer 1 -
I assumed that the framwork being used in the web project was Flask. I created a simple Flask backend just to process the data in the POST request and print the checkbox numbers. My very simple barebone HTML template file (Question 1/app/templates/form_submit.html) attempts to re-create the scenario in the question by creating a form that has 10 checkboxes and one 'Submit' button. My backend logic file (Question 1/app/views.py) contains the required code to parse the POST request and print the checkbox numbers.

Question 2 - 
You are given an array in Python, which contains positive integers and/or recursively nested arrays of positive integers. It may, for example, be initialized as:
arr = [[141,151,161],2,3,[101,202,[303,404]]]
Write a function def MaxArray(arr) which returns the maximum value contained in arr or some array nested within arr. In the example, the returned value should be 404.