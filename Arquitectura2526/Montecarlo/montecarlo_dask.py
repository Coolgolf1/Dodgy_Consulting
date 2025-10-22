"""
======================================================================
 Monte Carlo Simulation with Dask
======================================================================

Author:       Dodgy Consulting
File:         montecarlo_dask.py
Description:  This script performs a Monte Carlo simulation using the
              Dask distributed computing framework. It allows parallel
              sampling of random variables across multiple workers to
              estimate a given function's expected value or probability
              distribution.

Usage:
    python montecarlo_ray.py <num_samples>

    Example:
        python montecarlo_ray.py 1000000

Arguments:
    num_samples : int
        The number of random samples to generate in the simulation.

Dependencies:
    - Python >= 3.8
    - dask
    - numpy

Functions:
    - estimate_pi(n_samples)
    - main()

Version:      1.0
Date:         2025-10-02
======================================================================
"""

import os
import random
from dask.distributed import Client
import argparse
from time import perf_counter
from dotenv import load_dotenv
import matplotlib.pyplot as plt


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("t", type=int, help="Number of tasks for Dask.")

    args = parser.parse_args()

    load_dotenv("./../Practica/Escenario2/.env")

    port = os.getenv("DASKPORT")

    client = Client(f'localhost:{port}')

    n_tasks = args.t
    samples = [5000000, 10000000, 50000000]
    times = []
    results = []

    for sample in samples:
        print(f"===== Samples: {sample} | Tasks: {n_tasks} =====")

        start_time = perf_counter()

        futures = [client.submit(get_points_in_circle, sample//n_tasks).result()
                   for _ in range(n_tasks)]

        pi = 4 * sum(futures) / sample

        end_time = perf_counter()

        print(f"Pi: {pi}")
        print(f"Time taken: {end_time - start_time}")

        times.append(end_time - start_time)
        results.append(pi)

    plt.figure()
    plt.title(f"Time taken with {n_tasks} tasks")
    plt.plot(samples, times)
    plt.xlabel("Number of Samples")
    plt.ylabel("Time (s)")
    plt.savefig(f"./../Practica/Escenario2/figs/time_{n_tasks}.png")

    plt.figure()
    plt.title(f"Evolution of estimated value of pi with diferent samples")
    plt.plot(samples, results)
    plt.axhline(y=3.1415926535, color='r', linestyle='--',
                linewidth=2, label='y = π')
    plt.legend()
    plt.xlabel("Number of Samples")
    plt.ylabel("Estimation of Pi")
    plt.savefig(f"./../Practica/Escenario2/figs/pi_{n_tasks}.png")

    client.shutdown()


def get_points_in_circle(n_samples: int) -> int:
    """Get points in circle using Monte Carlo simulation.

    Args:
        n_samples (int): Number of random samples to generate.

    Returns:
        float: Number of points.
    """
    n_inside = 0
    for _ in range(n_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            n_inside += 1

    return n_inside


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        raise Exception(f"Error in runtime: {err}.")
