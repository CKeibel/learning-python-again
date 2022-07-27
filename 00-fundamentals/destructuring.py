
if __name__=="__main__":
    currencies = 0.8, 1.2
    usd, eur = currencies
    print(f"USD: {usd}\tEUR: {eur}")

    friends = [("Anne", 34), ("Tom", 31), ("Mark", 25), ("Jen", 28)]

    for name, age in friends:
        print(f"{name} is {age} years old.")

    # dictionary destructuring
    friends = {"Anne": 32, "Mark": 25, "Tom": 41, "Jen": 32}
    for key, value in friends.items():
        print(f"{key}: {value}")