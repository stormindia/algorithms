import time
import multiprocessing


def do_something(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    print('done sleeping')


if __name__ ==  '__main__' :        #necessary

    start = time.perf_counter()

    p1 = multiprocessing.Process(target = do_something, args =[2])
    p2 = multiprocessing.Process(target = do_something, args =[2])


    p1.start()
    p2.start()

    p1.join()
    p2.join()


    finish = time.perf_counter()

    print('finished in {} seconds'.format(finish - start))
