Package name: JSutils
Author: Jaime Loeuf
License: MIT
------------------------

Package Desciption:
This package contains a class that implements the setInterval function like the one in JavaScript.

To call a function over and over again with a fixed interval:
    >>> from JSutils import setInterval
	>>>
	>>> def HelloWorld(message):
	>>>		print('Hello world')
	>>>		print(message) # Print out / use the arguement.
	>>>
	>>>	setInterval(5, HelloWorld)