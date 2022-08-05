def main():
    # read
    file = open("read-write.txt", "r")
    data = file.read()
    file.close()
    print(data)

    # write
    user_input = input("Enter your name:")
    file = open("read-write.txt", "w")
    file.write(user_input)
    file.close()


if __name__ == "__main__":
    main()