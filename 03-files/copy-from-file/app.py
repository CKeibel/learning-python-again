def main():
    # Ask for 3 friends
    friends = input("Enter 3 friends comma separated: ").split(",")
    friends = [friend.strip().lower() for friend in friends]

    # Look if they are in "nearby_people.txt"
    people_file = open("nearby_people.txt", "r")
    people_nearby = [line.strip().lower() for line in people_file.readlines()]
    people_file.close()

    # copy nearby people to "nearby_friends.txt"
    friends_set= set(friends)
    people_nearby_set = set(people_nearby)
    friends_nearby = friends_set.intersection(people_nearby_set)

    friends_file = open("nearby_friends.txt", "w")
    for friend in friends_nearby:
        print(f"{friend.title()} is nearby!")
        friends_file.write(f"{friend.title()}\n")
    friends_file.close()


if __name__ == "__main__":
    main()
