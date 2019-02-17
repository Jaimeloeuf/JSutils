### Package name: JSutils

- Author: Jaime Loeuf
- License: MIT
- Package Desciption:
	- This package contains classes/functions that implements functions like the setInterval function from JavaScript.
	- This package currently does not have any external dependencies, written only with py std. lib
	- Currently this package contains the
		1. 'setInterval' class

##### To call a function over and over again with a fixed interval:
```python
from JSutils import setInterval

def HelloWorld(message):
	print('Hello world')
	print(message) # Print out / use the arguement.

setInterval(5, HelloWorld)
```