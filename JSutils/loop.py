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

        # self.task = Process(target=self.start)
        self.task = Thread(target=self.start)

        self.task.daemon = True  # Daemonize thread
        self.task.start()  # Start the execution

    def start(self):
        """ Method that runs forever until main process/thread is killed """
        
        from threading import Timer
        Timer.start()

        while flag.isSet:
            # sleep(self.__time)
            # self.fn(*self.args, **self.kwargs)

            sleep(self.__time)
            self.fn(*self.args, **self.kwargs)

    # Method to stop the loop, if needed, execute the callback one last time
    def stop(self, oneLastTime=False):
        # Kill the task first thing first
        # self.task.terminate() # Terminate is for Processes only
        # self.task.

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


def hello(msg):
    print('Chicken ', msg)

if __name__ == "__main__":
    # If this module called as a standalone module to see how it works, then run the below example code
    setInterval(1, hello, 'nuggets')

    while True:
        pass

    # This is a loop and sleep based setInterval commpared to a Timer Object based setInterval
