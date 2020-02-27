import threading
import time


start = time.perf_counter()


def do_something(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    print('done sleeping')


# t1 = threading.Thread(target=do_something)
#
# t2 = threading.Thread(target=do_something)
#
#
# t1.start()
# t1.join()
#
# t2.start()
# t2.join()

threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args = [2])   #2 is passed as an argument to do_something #also try writing target=do_something()
    t.start()
    threads.append(t)


for thread in threads:
    thread.join()



finish = time.perf_counter()

print('finished in {} seconds'.format(finish - start))
#print(threads)
