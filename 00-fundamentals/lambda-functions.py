if __name__ == "__main__":
    average = lambda sequence: sum(sequence) / len(sequence)

    sequences = [
        {"day1": [1, 4, 5, 8]},
        {"day2": [6, 24, 0, 18]},
        {"day3": [7, 3, 2, 8]},
        {"day4": [1, 7, 3, 1, 65]},
        {"day5": [90, 2, 5, 8, 5, 154]}
    ]

    for index, entry in enumerate(sequences):
        print(average(entry[f"day{index+1}"]))
