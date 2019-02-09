import sys
import os

# View all the environmental variables
# os.environ
print(os.environ)


# using get will return `None` if a key is not present rather than raise a `KeyError`
print(os.environ.get('KEY_THAT_MIGHT_EXIST'))

# os.getenv is equivalent, and can also give a default value instead of `None`
print(os.getenv('KEY_THAT_MIGHT_EXIST', default_value))

# Python default installation on Windows is C:\Python. Use below to find out
print(sys.prefix)

# To check if the key exists (returns True or False)
'HOME' in os.environ


"""
My python script which calls many python functions and shell scripts. I want to set a environment variable in Python (main calling function) and all the daughter processes including the shell scripts to see the environmental variable set.

I need to set some environmental variables like this:

DEBUSSY 1
FSDB 1
1 is a number, not a string. Additionally, how can I read the value stored in an environment variable? (Like DEBUSSY/FSDB in another python child script.)
"""

os.environ['DEBUSSY'] = '1'
os.environ['FSDB'] = '1'

# Open child processes via os.system(), popen() or fork() and execv()

# Then read the variable using the same method whilst in the child process
someVariable = int(os.environ['DEBUSSY'])
