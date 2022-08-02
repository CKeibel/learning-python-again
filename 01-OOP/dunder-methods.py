
class Garage:
    def __init__(self, cars = []):
        self.cars = cars

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        return self.cars[index]

    def __repr__(self):
        return f"<Garage {self.cars}>"

    def __str__(self):
        return f"Garage with {len(self)} cars."

def main():
    my_garage = Garage()
    my_garage.cars.append("Audi")
    my_garage.cars.append("Ford")

    print(len(my_garage))
    print(my_garage[1])
    print(my_garage)


if __name__ == "__main__":
    main()