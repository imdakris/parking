"""Program for registering cars and their drivers."""
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


def write_file(cars: dict) -> None:
    """Updates information about cars and drivers in a file"""
    with open("parking.txt", "w", encoding="utf-8") as file:
        for name, car in cars.items():
            file.writelines(f"{name}:{car}\n")


def parking() -> None:
    """registering cars and their drivers"""
    cars = read_or_create_file()
    while True:
        command = input(
            "1-Add\n"
            "2-Delete\n"
            "3-View\n"
            "4-Change\n"
            "5-Write to file\n"
            "Enter the command: "
        )
        if command == "1":
            owner = input("Enter owner name: ")
            if cars.get(owner):
                print(
                    f"The owner's car with the name {owner} is already in the parking lot."
                )
                continue
            car = input("Enter your car make: ")
            cars[owner] = car

        elif command == "2":
            owner = input("Enter owner name: ")
            if cars.get(owner):
                cars.pop(owner)
                print(f"{owner} left")

            else:
                print(f"No owner named {owner} was found")

        elif command == "3":
            for owner, car in cars.items():
                print(f"{owner}-{car}")

        elif command == "4":
            owner = input("Enter owner name: ")
            if cars.get(owner):
                car = input("Enter your car make: ")
                cars[owner] = car
            else:
                print(f"No owner named {owner} was found")

        elif command == "5":
            write_file(cars)
            print("Data recorded")


parking()
