import concurrent.futures
import time


def do_something(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'done sleeping {seconds} seconds'


if __name__ ==  '__main__' :        #necessary
    with concurrent.futures.ProcessPoolExecutor() as executor:

        seconds = [5,4,3,2,1]

        # p1 = executor.submit(do_something, 2)
        # p2 = executor.submit(do_something, 2)
        #
        # print(p1.result())
        # print(p2.result())

        # results = [executor.submit(do_something, sec) for sec in seconds]
        #
        # for result in concurrent.futures.as_completed(results):
        #     print (result.result())

        results = executor.map(do_something, seconds)
        for result in results:
            print(result)
