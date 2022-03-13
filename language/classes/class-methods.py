# some examples
class Pet:
	def __init__(self, name, color):
		self.name = name
		self.color = color

class Dog(Pet):
	def __init__(self, name, color, size):
		super().__init__(name, color)
		self.size = size
	
	def print_size(self):
		print("Size is: " + str(self.size))
	
	# alternative constructor example
	@classmethod
	def create_dog(cls, example_string):
		processed_string = example_string
		return cls(processed_string) # this way you can construct a class in an alternative way

	@staticmethod
	def print_hello():
		print("Hello")


Snoopy = Dog.create_dog(Pet, "snoopy-brown")
# this would call Pet