class MyCostumError(Exception):
    def __init__(self, message, code):
        super().__init__(f"{code} {message}")


def main():
    raise MyCostumError("There went something wrong.", 500)


if __name__ == "__main__":
    main()
