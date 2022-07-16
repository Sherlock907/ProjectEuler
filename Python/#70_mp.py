from time import perf_counter as _p
import multiprocessing
import sympy

def checkifperm(x,y):
    x = str(x)
    y = str(y)
    if sorted(x) == sorted(y):
        return True
    return False


def mp_worker(queue, nums):
    res = list()
    for i in nums:
        if checkifperm((x := sympy.totient(i)), i):
            res.append([i / x, i])
    queue.put(res)


def mp_main(n, processes):
    queue = multiprocessing.Queue()

    factor = len(n)//processes
    procs = []
    results = []

    for i in range(processes):
        if i == processes-1:
            proc = multiprocessing.Process(target=mp_worker, args=(queue, n[factor*i:]))
            procs.append(proc)
            proc.start()
        else:
            proc = multiprocessing.Process(target=mp_worker, args=(queue, n[factor*i:factor*i+factor]))
            procs.append(proc)
            proc.start()

    for i in range(processes):
        results += queue.get()

    for i in procs:
        i.join()

    return results


if __name__ == "__main__":
    _s = _p()
    res = mp_main([i for i in range(2,10**7)],8)
    print(min(res))
    print(_p() - _s)
    """
    Result : [1.0007090511248113, 8319823]
    Runtime: 117.84 s
    """
