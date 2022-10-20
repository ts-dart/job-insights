import csv
from functools import lru_cache


@lru_cache
def read(path):
    lines = []

    with open(path) as file:
        data = csv.DictReader(file)

        for index in data:
            lines.append(index)

    return lines
