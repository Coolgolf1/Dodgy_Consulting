"""
======================================================================
 Monte Carlo Simulation with Spark
======================================================================

Author:       Dodgy Consulting
File:         montecarlo_spark.py
Description:  This script performs a Monte Carlo simulation using the
              Spark distributed computing framework. It allows parallel
              sampling of random variables across multiple workers to
              estimate a given function's expected value or probability
              distribution.

Usage:
    python montecarlo_spark.py <num_samples>

    Example:
        python montecarlo_spark.py 1000000

Arguments:
    num_samples : int
        The number of random samples to generate in the simulation.

Dependencies:
    - Python >= 3.8
    - pyspark.sql
    - numpy

Functions:
    - estimate_pi(n_samples)
    - main()

Version:      1.0
Date:         2025-11-19
======================================================================
"""

from datetime import datetime
import os
import random
from pyspark.sql import SparkSession
from typing import List, Tuple
import argparse
from time import perf_counter


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("t", type=int, help="Number of tasks for Spark.")

    args = parser.parse_args()

    appdate = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    appName = "-".join(["Procesamiento", appdate])

    spark = SparkSession.builder.appName(appName).master(f"spark://spark-master:7077").config("spark.executor.memory", "2g").config("spark.driver.memory", "1g").getOrCreate()

    sc = spark.sparkContext

    n_tasks = args.t
    samples = [50000000, 100000000, 500000000]
    times = []
    results = []

    for sample in samples:
        print(f"===== Samples: {sample} | Tasks: {n_tasks} =====")

        start_time = perf_counter()

        rdd = sc.parallelize(range(sample), numSlices=n_tasks)

        rdd = rdd.map(lambda x: random.uniform(-1, 1)**2 + random.uniform(-1, 1)**2)        

        rdd = rdd.filter(lambda x: x <= 1)

        pi_values = rdd.count()

        pi = 4 * pi_values / sample

        end_time = perf_counter()

        print(f"Pi: {pi}")
        print(f"Time taken: {end_time - start_time}")

        times.append(end_time - start_time)
        results.append(pi)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        raise Exception(f"Error in runtime: {err}.")
