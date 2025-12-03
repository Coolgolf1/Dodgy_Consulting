import matplotlib.pyplot as plt
import os

path = os.path.join(
    os.getcwd(), "Arquitectura2526/Practica/Escenario3/figs/emr")

os.makedirs(path, exist_ok=True)

samples = [50_000_000, 100_000_000, 500_000_000]
n_tasks = 12
times = {
    # 1: [7.391664129000219, 7.479718485999911, 35.667089410000244],
    # 2: [5.971238573999926, 3.9717176190001737, 18.633847863000028],
    3: [14.629769378999981, 12.649507476000053, 57.51242304000016]
}
results = {
    # 1: [3.1423584, 3.1416132, 3.14158616],
    # 2: [3.1421688, 3.141952, 3.14176144],
    3: [3.14181864, 3.14169192, 3.141592144]
}
workers = [3]


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
