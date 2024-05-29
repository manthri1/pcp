import threading
import time
import queue
shared_queue=queue.Queue()
def producer():
    for i in range(10):
        data=f"data {i}"
        producer=f"producer:{data}"
        print(producer)
        shared_queue.put(data)
        time.sleep(1)
def consumer():
    while True:
        data=shared_queue.get()
        print(f"consumer: {data}")
        shared_queue.task_done()
        time.sleep(2)
producer_thread=threading.Thread(target=producer)
consumer_thread=threading.Thread(target=consumer)
producer_thread.start()
consumer_thread.start()
producer_thread.join()
shared_queue.join()
print("program finished")