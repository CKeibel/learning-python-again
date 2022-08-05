"""
csv to json converter
"""
import json


def convert(file: str):
    """
    :param file: full path to file
    :return: None
    """

    friends = []

    with open(file, "r") as file:
        content = [line.strip() for line in file.readlines()]
        for line in content:
            name, age, university = line.split(",")
            friend = {
                "name": name,
                "age": age,
                "university": university
            }

            friends.append(friend)
            print(f"added {friend}")

    with open("friends.json", "w") as file:
        json.dump(friends[1:], file)


def main():
    convert("data.csv")


if __name__ == "__main__":
    main()
