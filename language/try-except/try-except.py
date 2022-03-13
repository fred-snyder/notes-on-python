# try/except

try:
	# execute some code
	age = 12
except:
	# execute try block errors
	age = 40

# best pratice: catch a specific error
"""
except ZeroDevisionError:
	# some code
except ValueError:
	# some code
except ValueError as err:
	print(err) # print out the error that occured
"""
