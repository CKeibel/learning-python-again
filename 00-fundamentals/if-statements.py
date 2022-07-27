
if __name__=="__main__":
    friends = ["Anne", "Tom", "Mark"]
    family = ["Pascal", "Rolf"]

    user_input = input("Whats your name:")

    if user_input in friends:
        print("Hello friend!")
    elif user_input in family:
        print("Hello family!")
    else:
        print("Hello stranger!")