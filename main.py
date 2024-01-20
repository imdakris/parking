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
