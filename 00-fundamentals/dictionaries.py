
if __name__=="__main__":
    friends = (
        {"name": "Mark", "age": 34},
        {"name": "Tim", "age": 31},
        {"name": "Anne", "age": 35}
    )

    print(friends[0]["name"])

    friends = [("Rolf", 24), ("Jen", 29), ("Tom", 45)]
    friends_ages = dict(friends)
    print(friends_ages)