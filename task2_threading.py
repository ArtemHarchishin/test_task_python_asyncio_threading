import threading


def task(t, msg, sem):
    threading.Event().wait(t)
    sem.acquire()
    print(msg)
    sem.release()



def worker(t, msg, sem):
    t1 = threading.Thread(target=task, args=(t, msg, sem))
    t1.start()


def main():
    semaphore = threading.Semaphore(value=1)
    worker(1, '1', semaphore)
    worker(3, '2', semaphore)
    worker(5, '3', semaphore)


main()

