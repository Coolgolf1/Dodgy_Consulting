import matplotlib.pyplot as plt
import os

path = os.path.join(os.getcwd(), "Arquitectura2526/Practica/Escenario3/figs")

samples = [5000000, 10000000, 50000000]
n_tasks = 12
times = {
    1: [7.391664129000219, 7.479718485999911, 35.667089410000244],
    2: [5.971238573999926, 3.9717176190001737, 18.633847863000028],
    3: [7.695093987000291, 3.9029013600002145, 18.5237345810001]
}
results = {
    1: [3.1423584, 3.1416132, 3.14158616],
    2: [3.1421688, 3.141952, 3.14176144],
    3: [3.1410536, 3.1417736, 3.1414304]
}
workers = [1, 2, 3]


for worker in workers:
    for sample in samples:
        plt.figure()
        plt.title(f"Time taken with {n_tasks} tasks")
        plt.plot(samples, times[worker])
        plt.xlabel("Number of Samples")
        plt.ylabel("Time (s)")
        plt.savefig(f"{path}/time_{n_tasks}_{worker}w.png")

        plt.figure()
        plt.title(f"Evolution of estimated value of pi with diferent samples")
        plt.plot(samples, results[worker])
        plt.axhline(y=3.1415926535, color='r', linestyle='--',
                    linewidth=2, label='y = π')
        plt.legend()
        plt.xlabel("Number of Samples")
        plt.ylabel("Estimation of Pi")
        plt.savefig(
            f"{path}/pi_{n_tasks}_{worker}w.png")
