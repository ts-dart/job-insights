import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path) as file:
        data = csv.DictReader(file)
        lines = [index for index in data]

    return lines
