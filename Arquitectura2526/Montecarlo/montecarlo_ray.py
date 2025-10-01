import random
import ray
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("n", type=int,
                    help="Number of samples for Montecarlo simulation.")

args = parser.parse_args()

ray.init()


@ray.remote
def estimate_pi(n_samples: int) -> float:
    n_inside = 0
    for _ in range(n_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 <= 1:
            n_inside += 1

    pi = 4 * n_inside / n_samples

    return pi


if __name__ == "__main__":
    n_samples = args.n
    estimate_remote = estimate_pi.remote(n_samples)
    pi = ray.get(estimate_remote)
    print(pi)
