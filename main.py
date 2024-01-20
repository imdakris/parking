'''Program for registering cars and their drivers.'''
from pathlib import Path


def read_or_create_file() -> dict:
    """Reading and writing to a file"""
    f = Path("parking.txt")
    cars = {}
    if f.exists():
        with open("parking.txt", "r", encoding="utf-8") as file:
            for i in file.readlines():
                name, car = i[:-1].split(":")
                cars.update({name: car})

    else:
        file = open("parking.txt", "w", encoding="utf-8")
        file.close()
    return cars

