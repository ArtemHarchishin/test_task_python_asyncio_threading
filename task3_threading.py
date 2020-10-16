import threading


def task(t, msg, sem):
    """
    send msg after t seconds
    if t = 0 send msg every second
    """
    if not t:
        while True:
            threading.Event().wait(1)
            sem.acquire()
            print(msg)
            sem.release()
    
    threading.Event().wait(t)
    sem.acquire()
    print(msg)
    sem.release()


def worker(t, msg, sem):
    t1 = threading.Thread(target=task, args=(t, msg, sem))
    t1.start()


def main():
    semaphore = threading.Semaphore(value=1)
    worker(0, '1', semaphore)
    worker(1, '2', semaphore)
    worker(3, '3', semaphore)


main()

