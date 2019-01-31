# import threading
from threading import Thread
from multiprocessing import Process
from time import sleep


# class ThreadingExample(object):
#     """ Threading example class
#     The run() method will be started and it will run in the background
#     until the application exits.
#     """

#     def __init__(self, interval=1, msg=None):
#         """ Constructor
#         :type interval: int
#         :param interval: Check interval, in seconds
#         """
#         self.interval = interval
#         self.msg = msg

#         thread = threading.Thread(target=self.run, args=())
#         thread.daemon = True                            # Daemonize thread

#         # thread = Process(target=self.run, args=())
#         # thread.daemon = True                            # Daemonize thread

#         thread.start()                                  # Start the execution

#     def run(self):
#         """ Method that runs forever """
#         while True:
#             # Do something
#             print(self.msg)

#             sleep(self.interval)


class setInterval:
    """ setInterval Class:
        This is used to create a type of loop, where a given function/method is called repeatedly every
        'n' given seconds, until the stop method is called, or when the main thread dies/exits. Used this
        to emulate the behaviour of the native setInterval function in JavaScript.

        When we say run this every 10 Seconds. Do we mean to execute the program every 10 seconds or do we mean to
        have 10 seconds time interval between the end of function execution 1 and the start of function execution 2?

        How does my other loop deal with this?
        """

    # To pass in the interval time, callback function, and any arguements for the callback function into the constructor
    def __init__(self, time, fn, *args, **kwargs):
        self.__time = time
        self.__fn = fn
        self.__args = args
        self.__kwargs = kwargs
        # Start looping
        self.start()

    # Wrapper method for the loop. Should not be called externally or by any other method except the start method
    def _loop(self):
        # Loop that runs forever until this process is killed
        while True:
            # Sleep first before calling the function.
            sleep(self.__time)
            self.__fn(*self.__args, **self.__kwargs)

    def start(self):
        """ Method that calls the infinite loop's wrapper function """
        # Create a new child process to run the infinite loop to make it non blocking.
        self.__loop_process = Process(target=self._loop)
        self.__loop_process.daemon = True # Daemonize the process, so when the main process dies, it is killed too.
        self.__loop_process.start() # Start the execution within the child process

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
