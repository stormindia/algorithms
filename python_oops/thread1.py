import concurrent.futures

import time


start = time.perf_counter()


def do_something(seconds):
    print(f'sleeping for {seconds} seconds')
    time.sleep(seconds)
    return f'done sleeping {seconds} seconds'



with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 1)
    # f2 = executor.submit(do_something, 1)
    # print(f1.result())
    # print(f2.result())
    second = [5,4,3,2,1]
    #results = [executor.submit(do_something, sec) for sec in second]
    results = executor.map(do_something, second)

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    for result in results:
        print(result)


finish = time.perf_counter()

print('finished in {} seconds'.format(finish - start))
