
if __name__=="__main__":
    friends = {"Tim", "Anne"}
    friends.add("Sven")
    print(friends)
    friends.remove("Anne")
    print(friends)

    art_friends = {"Tom", "Anne", "Jen"}
    science_friends = {"Sven", "Tom", "Anne", "Mark"}

    art_only = art_friends.difference(science_friends)
    print(art_only)
    science_only = science_friends.difference(art_friends)
    print(science_only)

    not_in_both = science_friends.symmetric_difference(art_friends)
    print(not_in_both)

    all = art_friends.union(science_friends)
    print(all)

