# Classes

> (Almost) everything in Python is an object. (int, str, etc)

Python OOP, Corey Schafer:
- https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
- https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc


## Some definitions:

- A class is a template for a user-defined data structure
    - It's a blueprint for creating an object
    - An object is an instance of a class
    - A class has attributes (variables) and methods (functions)


## Class inheritance

- A class can inherit attributes and methods from a parent class. So a class that inherits from another class is a subclass.
- A subclass can overwrite or create new functionality without affecting the parent class.


## Output information about objects and classes
```python

print(help(Asset))
# will show you for example: the "method resolution order"

className.__dict__()
Asset.__dict__()
# this will show you all the instance variables

isinstance(instance_or_objectName, ClassName)
issubclass(subClassName, ClassName)
```
https://www.youtube.com/watch?v=C-gEQdGVXbk
check min 34
corey shows how to use the dir function


```python
# A class is a template or blueprint for a user-defined data structure

# this way of declaring the class variables is very cumbersome but it explains how the "self" part works.
class Student:
	def __init__(self, class_attribute_name, class_attribute_major, class_attribute_gpa):
		self.class_var_name = attribute_name
		self.class_var_major = attribute_major
		self.class_var_gpa = attribute_gpa

# the convention for declaring class variables is in the following way:
class Student:
	def __init__(self, name, major, gpa):
		self.name = name
		self.major = major
		self.gpa = gpa

	# this functions is a piece of code that checks something for you.
	# you could set an on_honor_roll boolean variable when creating the student object
	# but this function just follows the protocol for checking if a student is on honor-roll
	def on_honor_roll(self):
		if self.gpa >= 3.5:
			return True
		else:
			return False

# class inheritance
class HighSchoolStudent(Student):
		# this class inherits from the Student class
		# and overrides the on_honor_roll method
		def on_honor_roll(self):
			if self.gpa >= 3:
				return True
			else:
				return False


from Student.py import Student
# does this work as well? # from Student.py import Student

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)
```
