class Event(object):

    def __init__(self):
        self.handlers = []

    def add(self, handler):
        self.handlers.append(handler)
        return self

    def remove(self, handler):
        self.handlers.remove(handler)
        return self

    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, earg)

    __iadd__ = add
    __isub__ = remove
    __call__ = fire

"""
The last 3-line-code enables you to write your code like
	e += handler
	e -= handler
	e(earg)	
instead of
	e.add(handler)
	e.remove(handler)
	e.fire(earg)
"""


class Event(object):
    def __init__(self):
        self.handlers = []

	@property
    def add(self, handler):
        self.handlers.append(handler)
        return self

	@handlers.property
    def remove(self, handler):
        self.handlers.remove(handler)
        return self

	@property
    def fire(self, sender, earg=None):
        for handler in self.handlers:
            handler(sender, earg)

    __iadd__ = add
    __isub__ = remove
    __call__ = fire
