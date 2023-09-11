"""
A runner to benchmark the performance of algorithms in Python.
"""

import argparse
import time

from search_sort.insertion_sort import insertion_sort
from search_sort.bubble_sort import bubble_sort

from utils.array_utils import load_arrays_from_csv

def benchmark_algorithm(algorithm, data):
    start_time = time.time()
    sorted_data = algorithm(data)
    elapsed_time = time.time() - start_time
    return sorted_data, elapsed_time

def run_benchmark(benchmark_name):
    test_suite = load_arrays_from_csv('data/1000_tests_of_array_size_1000.csv')
    
    total_time = 0

    if benchmark_name == "insertion_sort":
        algorithm = insertion_sort
    elif benchmark_name == "bubble_sort":
        algorithm = bubble_sort
    else:
        print(f"No benchmark found for: {benchmark_name}")
        return

    for test_data in test_suite:
        _, elapsed_time = benchmark_algorithm(algorithm, test_data)
        total_time += elapsed_time

    avg_time = total_time / len(test_suite)
    print(f"Total time taken for {benchmark_name} over {len(test_suite)} tests: {total_time:.5f} seconds")
    print(f"Average time taken for {benchmark_name} over {len(test_suite)} tests: {avg_time:.5f} seconds")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run benchmarks for algorithms in Python.")
    parser.add_argument("benchmark", help="Name of the benchmark to run. (e.g., insertion_sort)")

    args = parser.parse_args()
    run_benchmark(args.benchmark)
