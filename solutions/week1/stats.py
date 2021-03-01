#!/usr/bin/env python3
import sys
import statistics
from collections import Counter

def average(n):
    """
    Average of values in a list
    :param n: List of numbers
    :return: float
    """
    aver = sum(n)/len(n)
    return aver

def median(n):
    """
    Median of values in a list
    :param n: List of numbers
    :return: float
    """
    med = statistics.median(n)
    return med


def mode(n):
    """
    Mode of values in a list
    :param n: List of numbers
    :return: float
    """
    mod = Counter(n).most_common(1)[0][0]
    return mod


def open_files(name_file):
    # Try to code this section
    """
    Description
    :param name_file:
    :return: list of numbers
    """
    pass


def main(args):

    if '--file' in args:
        print('Placeholder for --file \nThis flag does nothing at the moment')
        return 0
    else:
        numbers = []
        for num in args:
            try:
                numbers.append(float(num))
            except:
                pass
    

    if "--average" in args:
        print(f'Average: {average(numbers)}')
    if "--median" in args:
        print(f'Median: {median(numbers)}')
    if "--mode" in args:
        print(f'Mode: {mode(numbers)}')

    if len(args) == len(numbers):
        print(f'Average: {average(numbers)}')
        print(f'Median: {median(numbers)}')
        print(f'Mode: {mode(numbers)}')



if __name__ == "__main__":
    main(sys.argv[1:])