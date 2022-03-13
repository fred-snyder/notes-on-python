class Asset:
	def __init__(self, name, description):
		self.name = name
		self.description = description

class AssetVariant(Asset):
	def __init__(self, name, description, filename, filetype, filepath, tags=None):
		super().__init__(name, description):
		# Asset.__init__(self, name, description) # this is a less DRY approach
		self.filename = filename
		self.filetype = filetype
		self.filepath = filepath

		# never pass mutable data types as default arguments
		if tags is None: # note: "is" not "=="
			self.tags = []
		else:
			self.tags = tags

	def add_tag(self, tag):
		if tag not in self.tags: # check if tag is not already added
			self.tags.append(tag)

	def remove_tag(self, tag):
		if tag in self.tags: # check if tag exists
			self.tags.remove(tag)

	def print_tags(self):
		for tag in self.tags:
			print(tag)

# above approach is preferred. Easier to see which class is parent
class AssetAlternativeVariant:
	def __init__(self):
		# this way you call super on a specific class
		super(Asset, self).__init__(arguments)