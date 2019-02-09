""" Dependencies """
import os
import sys


# Function to get environmental variables. Returns value or None if none found
def get_env_var(var):
	return os.environ.get(var)


# Function to set environmental variables. Returns the value using the the get_env_var function
def set_env_var(var, value):
	os.environ[var] = value
	return get_env_var(var)




# Run the below example codes if module ran as the main module
if __name__ == "__main__":
	""" Below example code uses native functions/packages """
	# To view all the environmental variables. Note quite alot will be printed out.
	# print(os.environ)

	# Using get will return `None` if a key is not present rather than raise a `KeyError`
	print(os.environ.get('KEY_THAT_MIGHT_EXIST'))

	# os.getenv is equivalent, but a default value can also be used instead of `None`
	print(os.getenv('KEY_THAT_MIGHT_EXIST', 'DEFAULT VALUE'))

	# Python default installation on Windows is C:\Python. Use below to find out
	print(sys.prefix)

	# To check if the key exists (returns True or False)
	print('HOME' in os.environ)


	"""
	If your python script calls other python functions / shell scripts,
	you can set environment variables in the main python calling script's function,
	and have all the child processes including shell scripts to see them.
	"""

	# Set the environmental variables first
	os.environ['FOO'] = '1'
	os.environ['BAR'] = '2'

	# Open your child processes via os.system(), popen() or fork() and execv() or whatever other method you want

	# Then read the variable using the same method whilst in the child process
	env_var1 = os.environ['FOO']

	# Since a string is read in, if you want the int version, you will need to parse it out
	env_var2 = int(os.environ['BAR'])


	""" Below example code uses functions defined in this module itself """
	