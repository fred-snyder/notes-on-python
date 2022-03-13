class Student:
	def __init__(self, firstname, lastname, major, gpa):
		self.firstname = firstname
		self.lastname = lastname
		self.major = major
		self.gpa = gpa

	@property # property decorator # access this method as an attribute
	def fullname(self):
		return f'{self.firstname} {self.lastname}'

	@fullname.setter # setter decorator # set the attribute
	def fullname(self, fullname):
		first, last = fullname.split(' ')
		self.firstname = firstname
		self.lastname = lastname

	@fullname.deleter # deleter decorator # set an attribute to None
	def fullname(self):
		self.firstname = None
		self.lastname = None
