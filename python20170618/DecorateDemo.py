from datetime import datetime
import time


def timmer(func):
    def wrapper():
        start = time.time();
        func();
        end = time.time()
        print(end - start)
    return wrapper
@timmer
def test():
    time.sleep(3)
    time1 = datetime.now()
    print(time1)


test()