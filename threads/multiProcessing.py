#in multi process programming a thread uses its own shared memory and variables
# each thread runs its own memory space
# there is no shared memory
# this makes one process for each python process in task manager when multiprocessing executes
# Faster than threading
   # Reason is that this does not lock the code and this creates that code's binary code for each process

#first change thread to process

from multiprocessing import Process

class ImageDownloader(process)

 def __init__(self, process_id, name, result):
  pass

 def run(self):

