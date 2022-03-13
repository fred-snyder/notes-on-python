class Project:
	def __init__(self, name, slug, description, address=None, specs=None):
		self.name = name
		self.slug = slug
		self.description = description
		
		### specs
		# never pass mutable data types as default arguments
		if specs is None: # note: "is" not "=="
			self.specs = []
		else:
			self.specs = specs

		### address
		if address is None: # note: "is" not "=="
			self.address = []
		else:
			self.address = address

	def print_projectname(self):
		print(self.name)

	def add_address(self, address):
		if address not in self.address:
			self.address.append(address)
		else:
			print("Address already added")

	def add_specs(self, specs):
		if specs not in self.specs:
			self.specs.append(specs)
		else:
			print("Spec already added")


class Address:
	def __init__(self, streetname, zipcode, city, district):
		self.streetname = streetname
		self.zipcode = zipcode
		self.city = city
		self.district = district


class Specs:
	def __init__(self, floors, bedrooms, area):
		self.floors = floors
		self.bedrooms = bedrooms
		self.area = area
