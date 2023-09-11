import csv
import random

def generate_and_save_arrays_to_csv(filename, num_tests=100, array_size=1000, value_range=(1, 1000)):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(num_tests):
            array = [str(random.randint(value_range[0], value_range[1])) for _ in range(array_size)]
            writer.writerow(array)

# Call the function to generate the CSV
generate_and_save_arrays_to_csv('test_data.csv')

def load_arrays_from_csv(filename):
    arrays = []
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            arrays.append([int(item) for item in row])
    return arrays


if __name__ == "__main__":
    generate_and_save_arrays_to_csv('test_data.csv')