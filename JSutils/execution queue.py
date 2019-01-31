# import threading
from threading import Thread
from multiprocessing import Process
from time import sleep

""" Allows user to create a infinite loop to execute a few tasks repeatedly in a child process. """


class ExecQue:
    """ This is used to create a type of loop, where a given function/method is called repeatedly every
        'n' given seconds, until the stop method is called, or when the main thread dies/exits. Used this
        to emulate the behaviour of the native setInterval function in JavaScript.
        """

    # To pass in the interval time, callback function, and any arguements for the callback function into the constructor
    def __init__(self, time, fn_list, *args, **kwargs):
        self.__time = time
        # fn_list should be a list of dictionaries, where each dictionary contains the function reference and its args
        self.__fn = fn_list
        self.__args = args
        self.__kwargs = kwargs
        # Start looping
        self.start()

    # Method to append functions to the back of the execution queue
    def append_fn(self, fn, *args, **kwargs):
        self.__fn.append({
            "fn": fn,
            "args": args,
            "kwargs": kwargs
        })

    # Wrapper method for the loop. Should not be called externally or by any other method except the start method
    def _loop(self):
        # Loop that runs forever until this process is killed
        while True:
            # Sleep first before calling the function.
            sleep(self.__time)
            # Run all the functions in sequence
            for fn in self.__fn:
                fn(*self.__args, **self.__kwargs)

    def start(self):
        """ Method that calls the infinite loop's wrapper function """
        # Create a new child process to run the infinite loop to make it non blocking.
        self.__loop_process = Process(target=self._loop)
        # Daemonize the process, so when the main process dies, it is killed too.
        self.__loop_process.daemon = True
        self.__loop_process.start()  # Start the execution within the child process

    # Method to stop the loop, if needed, execute the callback one last time
    def stop(self, oneLastTime=False):
        # Kill the loop process first thing first
        self.__loop_process.terminate()  # Terminate is for Processes only

        # If 'oneLastTime' is True, Call the given function with any arguements supplied for the last time.
        if oneLastTime:
            self.__fn(*self.__args, **self.__kwargs)

    def restart(self):
        # Stop/Kill the current loop process
        self.stop()
        # Create a new Process to run the loop
        self.start()

    # Set/Change the interval for which the timer takes to timeout. New interval will start immediately.
    def set_interval(self, time):
        """ May be slow as the old process is killed and a new Process needs to be respawned """
        # Set the time into the object's field
        self.__time = time
        # Start new loop with new attributes
        self.restart()

    # Set the arguements to be passed into the callback function
    def set_args(self, *args, **kwargs):
        # Set the input arguements into the object's fields.
        self.__args = args
        self.__kwargs = kwargs
        # Start new loop with new attributes
        self.restart()


def hello(msg, invald_input=None, optionalMsg=None):
    print('Chicken ', msg, ' ', optionalMsg)


if __name__ == "__main__":
    # If this module called as a standalone module to see how it works, then run the below example code
    intervaloop = setInterval(1, hello, 'nuggets')

    sleep(3)

    intervaloop.set_interval(0.1)
    # intervaloop.set_args('hello', optionalMsg='HELAoscbnknjkjn')

    sleep(3)

    intervaloop.stop()
    # This is a loop and sleep based setInterval commpared to a Timer Object based setInterval
