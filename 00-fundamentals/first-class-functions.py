
operations = {
    "avg": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)
}

students = [
    {"name": "Bob", "grades": [95, 86, 100, 77]},
    {"name": "Jen", "grades": [90, 95, 70, 80]},
    {"name": "Mark", "grades": [89, 71, 55, 95]},
    {"name": "Anne", "grades": [93, 75, 96, 91]}
]


if __name__=="__main__":

    for student in students:
        print(student["name"])

        option = input("Choose between avg, total and top:")

        try:
            result = operations[option](student["grades"])
            print(result)
        except KeyError:
            print("Selection was notr valid.")