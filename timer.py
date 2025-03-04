"""
File: timer.py
Author: Alec Hoelscher with help from Github Copilot
Date: 03/03/2024
Description: Implementation of a timer decorator 

NOTE: Commented lines may be uncommented to print results in milliseconds or microseconds.
NOTE: Output format may need to be modified.
"""

import time
from functools import wraps
from typing import Callable

def timer(func: Callable) -> Callable:
    """Decorator function used to calculate execution time of a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds")
        # elapsed_time_ms = elapsed_time * 1000
        # print(f"Function '{func.__name__}' executed in {elapsed_time_ms:.4f} milliseconds")
        # elapsed_time_us = elapsed_time * 1000000
        # print(f"Function '{func.__name__}' executed in {elapsed_time_us:.4f} microseconds")
        return result
    return wrapper