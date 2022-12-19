'''
File to store Global variables

Some Notes : 
- global variable using keywork global is not recommended
- global static variables can be handeled nicely with pydotenv
- good practice is to use the (anti)pattern : singleton
  - A singleton can be coded in various ways : https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python
  - lets use the most simple one for now and just use this module as a singleton
'''

var_x = 0
var_y = 1
globalmodel = None