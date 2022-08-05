import json


def read_json():
    json_file = open("json.txt", "r")
    json_content = json.load(json_file)
    json_file.close()

    print(f"Type: {type(json_content)}\nContent: {json_content}")


def write_json():
    friends = [
        {
            "name": "Rolf",
            "age": 31
        },
        {
            "name": "Anne",
            "age": 35
        }
    ]

    file = open("friends.json", "w")
    json.dump(friends, file)
    file.close()



def main():
    read_json()
    write_json()


if __name__ == "__main__":
    main()
