
import threading
import thread
import time

lock = threading.Lock()
seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ino = 0

def message(L):
        global ino

        while ino <= 9:
            with lock:
                print L[ino]
                ino = ino + 1

thread.start_new_thread(message, (seq,))
thread.start_new_thread(message, (seq,))

time.sleep(3)
