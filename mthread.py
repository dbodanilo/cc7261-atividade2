import sympy
import concurrent.futures


def tCalculaPrimo(data):
    primos = 0
    for i in range(len(data)):
        if sympy.isprime(data[i]):
            primos += 1
    return primos

def resolve_thread(data, numThreads):
    ThreadsQtdd = numThreads
    tamanholista = len(data)
    index = []
    j = 0
    for i in range(0, tamanholista+1, tamanholista//ThreadsQtdd):
        index.append(i)
        j += 1

    index[-1] = tamanholista

    primos = 0
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(ThreadsQtdd):
            futures.append(executor.submit(tCalculaPrimo, data=data[index[i]:index[i+1]]))
        for future in concurrent.futures.as_completed(futures):
            #futures.append(future.result())
            primos += future.result()
    return primos
