"""
File: test_data.py
Author: Alec Hoelscher with help from Github Copilot
Date: 03/03/2024
Description: program to generate a json file filled with 100,000 random integers

NOTE: The name of the output file is data.json
"""

import json
import random

def generate_random_integers(seed, count, min_value, max_value) -> list:
    """Function to generate a list of random integers from min_value to max_value, uses seed to randomize"""
    random.seed(seed)
    return [random.randint(min_value, max_value) for _ in range(count)]

def write_to_json_file(data, filename):
    """Function to write the list to a json file"""
    with open(filename, 'w') as file:
        json.dump(data, file)

# This line ensures the code inside will only execute when this file is ran directly
if __name__ == "__main__":
    """Generating the random integers and outputting the json file"""
    seed = 12345
    count = 100000
    min_value = 0
    max_value = 1000000
    random_integers = generate_random_integers(seed, count, min_value, max_value)
    write_to_json_file(random_integers, 'data.json')