"""
======================================================================
 Monte Carlo Simulation with Ray
======================================================================

Author:       Dodgy Consulting
File:         montecarlo_ray.py
Description:  This script performs a Monte Carlo simulation using the
              Ray distributed computing framework. It allows parallel
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
    - ray
    - numpy

Functions:
    - estimate_pi(n_samples)
    - main()

Version:      1.0
Date:         2025-10-02
======================================================================
"""


import random
import ray
import argparse


def main() -> None:
    parser = argparse.ArgumentParser()


def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument("n", type=int,
                        help="Number of samples for Monte Carlo simulation.")
    parser.add_argument("n", type=int,
                        help="Number of samples for Monte Carlo simulation.")

    args = parser.parse_args()
    args = parser.parse_args()

    ray.init()
    ray.init()

    n_samples = args.n
    estimate_remote = estimate_pi.remote(n_samples)
    pi = ray.get(estimate_remote)
    print(pi)

    n_samples = args.n
    estimate_remote = estimate_pi.remote(n_samples)
    pi = ray.get(estimate_remote)
    print(pi)


@ray.remote
def estimate_pi(n_samples: int) -> float:
    """Estimates pi from Monte Carlo simulation.

    Args:
        n_samples (int): Number of random samples to generate.

    Returns:
        float: Estimate of pi.
    """
    """Estimates pi from Monte Carlo simulation.

    Args:
        n_samples (int): Number of random samples to generate.

    Returns:
        float: Estimate of pi.
    """
    n_inside = 0
    for _ in range(n_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            n_inside += 1

    pi = 4 * n_inside / n_samples

    return pi


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        raise Exception(f"Error in runtime: {err}.")
    try:
        main()
    except Exception as err:
        raise Exception(f"Error in runtime: {err}.")
