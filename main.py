from time import perf_counter_ns
import simples as sp
import mthread as mt

with open("data3.csv") as file:
    data = [line.strip() for line in file]

data = list(map(int, data))

print('\n\nanalise de %d valores\n\n'%(len(data)))

n = 50
sum_simples = 0

for j in range(0, n):
    start1 = perf_counter_ns()
    primo_sp = sp.resolve_simples(data)
    finish1 = perf_counter_ns()
    sum_simples += finish1 - start1

avg_simples = sum_simples / n

for i in [2, 4, 16, 256]:
    sum_thread = 0
    print("%d threads"%(i))
    print("%d execucoes"%(n))
    
    for j in range(0, n):
        start2 = perf_counter_ns()
        primo_mt = mt.resolve_thread(data, i)
        finish2 = perf_counter_ns()
        sum_thread += finish2 - start2

    avg_thread = sum_thread / n


    print('simples          > threads')
    print('%f ms   > %f ms  : tempo execucao'%(avg_simples/1000000, avg_thread/1000000))
    print('%d            > %d           :numeros primos encontrados'%(primo_sp,primo_mt))
    print("SpeedUp = %f"%(avg_simples/avg_thread))
    print("---\n")

