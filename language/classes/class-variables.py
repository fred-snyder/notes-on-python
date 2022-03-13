# class variables

class Test:
		cls_var = 'test'

		def someMethod(self):
				return self.cls_var
				# or # return Test.cls_var

# with self.cls_var you can override the variable per object/instance

test1 = Test()
test1.cls_var = 'override'
# if someMethod return Test.cls_var
# you can still override the variable but it's applied to every instance
			