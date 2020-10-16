import threading



def worker(t, msg):
    timer = threading.Timer(t, lambda: print(msg))
    timer.start()
    timer.join()


def main():
    worker(3, '1')
    worker(3, '2')
    worker(3, '3')


main()

