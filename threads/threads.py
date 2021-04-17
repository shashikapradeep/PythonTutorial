# This is something executes a set of codes.
# Example is like a counter in a bank.
# One counter does one set of activities repeatedly. Queue is the task.
# So if one core in a cpu done 2 jobs then 8 core computer does 16 jobs in parallel.
# New class should be made to run a thread
# thread.start() starts the thread
# then keep all threads in a list and merge all with join function and it will join all threads together once a thread has run
# at this time it waits until all threads have finished.

# multi threads are using same memory space. Its called shared memory. There are two ways
  # define a variable in main program (__main__) which threads run in and use it in a thread.
  # if threads are running in a different module, that variable should be injected to the thread.

# thread safe
# --------------
# python in-build data structures are thread safe. Thread safe means compatible to access a variable or method by multiple threads at the same time

# without using normal data structures, there are more data structures which made for Threads especially.
# They are
# 1. Queue

# A method can be accessed by only one thread at a time. Otherwise it makes some serious errors. So it makes lock that bite code
   #mutex - other languages
   #Global interpreter lock - python

from threading import Thread

class ImageDownloader(Thread):
 def __init__(self, thread_id, name):
  super(ImageDownloader, self).__init__()

 def run(self):
  pass


