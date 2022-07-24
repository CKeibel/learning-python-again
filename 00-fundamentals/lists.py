
if __name__=="__main__":
    friends_and_ages = [["Tim", 24], ["Tom", 45], ["Mark", 37]]
    print(friends_and_ages[2])
    print(friends_and_ages[0][1])

    friends_and_ages.append(["Pascal", 31])
    print(friends_and_ages)

    friends_and_ages.remove(["Tim", 24])
    print(friends_and_ages)