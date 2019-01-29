from threading import Timer, Thread

""" @Todos
    - Create a method that will call the stop method when the process exits. Because the timer thread continues to run
      even if the main program/thread is killed by keyboard interrupt, which means that the stop method is never called.
    - Create a method that allows user to specify if the interval should start running immediately. Meaning that I can create
      the interval and store the reference first without letting it run, this is so to allow me to do some settings/changes to
      the object first, or to allow user to only execute this 'loop' when certain conditions are met.
    - Create a method/check for the user to specify how many times this interval should run. So example would be, I only
      want this interval based loop to loop a maximum of 10 times before I want it to automatically stop.
      Or perhaps a time limit for how long this loop should loop for, like loopFor(10mins), meaning after 10 mins, the loop
      should call self.stop method. This can be possibly implemented by using another 'kill interval' timer that calls the
      stop method upon timeout.
    - Since this module is based on the Timer Class from the threading library, and based on threads, it is not advised to
      use this setInterval Class when doing actions that are CPU intensive and blocking on other threads, which may interfere
      with the timing of this Class. Will be working on another class based on the same idea that will run in a seperate
      process instead to allow true parallel and non concurrent execution style.
"""


class setInterval:
    """ setInterval Class:
        This is used to create a type of loop, where a given function/method is called repeatedly every
        'n' given seconds, until the stop method is called, or when the main thread dies/exits. Used this
        to emulate the behaviour of the native setInterval function in JavaScript.
        """

    # To pass in the interval time, callback function, and any arguements for the callback function into the constructor
    def __init__(self, time, fn, *args, **kwargs):
        self.__time = time
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        # Instead of calling input function on object creation, wait till end of the 1st time interval.
        # Delay the first call to the timeout method by the given time interval
        # self.__thread = Thread(target=self.start) # Testing to use threads, so I can make it a daemon to die on main thread exits.

        self.start()

    # Method to start the timer
    def start(self):
        self.__t = Timer(self.__time, self.timeOut)
        self.__t.start()
        # Return self to allow the user to do method call chainging. E.g. loop = setInterval(3, fn).start()
        return self

    # Method that is run everytime the Timer time's out.
    def timeOut(self):
        # Call the given function with any arguements supplied
        self.fn(*self.args, **self.kwargs)
        # Call start method to create another Timer object to call this function again on timeout.
        self.start()

    # Method to stop the loop, if needed, execute the callback one last time
    def stop(self, oneLastTime=False):
        # Kill the timer that repeatedly calls the timeOut method.
        self.__t.cancel()
        # If 'oneLastTime' is True, Call the given function with any arguements supplied for the last time.
        if oneLastTime:
            self.fn(*self.args, **self.kwargs)

    # Set/Change the interval for which the timer takes to timeout. New interval will start immediately.
    def set_interval(self, time):
        # Stop the current timer
        self.stop()
        # Set the time into the object's field
        self.__time = time
        # Reset the timer with a newly created Timer object using start method.
        self.start()

    # Set the arguements to be passed into the callback function
    def set_args(self, *args, **kwargs):
        # Set the input arguements into the object's fields.
        self.args = args
        self.kwargs = kwargs


if __name__ == "__main__":
    # If this module called as a standalone module to see how it works, then run the below example code
    from time import sleep

    # Print out the docs for setInterval in formatted doc strings
    # help(setInterval)

    def hi(val):
        print(val)

    try:
        tout = setInterval(1, hi, 'hei')
        sleep(3)

        tout.set_interval(0.1)
        sleep(2)

        tout.set_interval(1)
        tout.set_args('Nuggets')
        sleep(3)

    except (KeyboardInterrupt, SystemExit):
        # Stop the interval, but execute the callback one last time before killing the loop
        tout.stop(True)

    tout.stop(True)

    # If the keyboard interrupts at any time
    # except KeyboardInterrupt:
