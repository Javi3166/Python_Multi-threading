from threading import Thread, Lock, current_thread
from queue import Queue
import time

def worker(q):
    while True:
        value = q.get()
        # processing...
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        # daemon thread helps prevent the program from getting stuck on the true loop in the worker block
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        q.put(i)

    q.join()

    print("End Program")