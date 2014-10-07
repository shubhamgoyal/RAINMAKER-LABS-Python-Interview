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

Question 3 -
Write a function declared as def SplitEmailAddress(address), whose argument will contain string data consisting of a valid e-mail address. This function will take the email address as the argument and return a dictionary with two keys: user for the username part and domain for the domain part of the address. For example, after calling:
dict = SplitEmailAddress('myuser_1@mailserver.example.com') 
dict['user'] should contain the string myuser_1, and  dict['domain'] should contain the string mailserver.example.com

Question 4 -
Write a function GetLongestString, whose arguments are character strings. It should return an integer representing the length of the longest string passed as its argument; for example:
GetLongestString("a", "aaa", "aa") should return 3,
GetLongestString("a", "bcd", "efgh", "ij", "") should return 4. 

Question 5 -
Write a function GetUniqueOnes, which accepts a single argument. The argument is an array of integers, and the function should return the unique integers separated by commas.
For Example : GetUniqueOnes(arr) 
arr = [34,54,67,68,141,151,161,141,54,151,54]
should return 
34,54,67,68,141,151,161

Question 6 -
Write a function ReadXml(xmlstr) which accepts an XML string as its only argument. Your function should write the names of the nodes and their values. 
For Example : 
ReadXml(xmlstr) where 
xmlstr= '<Address><to>James</to><from>Jani</from><heading>Reminder</heading><body>Please check your mail.</body></Address>' 
should return 
Address
to: James
from: Jani
heading: Reminder
body: Please check your mail.
Note: As the question requires the output to be displayed in the new/ next line, use "\n" instead of "<br>"

Question 7 -
Consider a database with one table called "user" having two fields:
"id" (type: INTEGER, PRIMARY KEY) 
"name" (type: VARCHAR(32))
Write a standard SQL query which retrieves the second highest value of "id" from the "user" table. The value returned should be represented using the column name "id".

Question 8 -
Write a function GeneratePassword which accepts two arguments, an integer and a character string consisting of letters (a-z) and digits (0-9).
When GeneratePassword(5,'abc0123') is called, it should return a random string of 5 characters taken from 'abc0123'. 
For Example : GeneratePassword(7,'abczxc012394') could return any of the following outputs : 
2c00acb 
2c23z93 
030b2a4

Question 9 -
Write a program that outputs the numbers that are divisible by 8 and are between 200 and 600 (inclusive), separated by commas (without spaces or line breaks).