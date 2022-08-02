
class Garage:
    def __init__(self, cars = []):
        self.cars = cars

    def __len__(self):
        return len(self.cars)

def main():
    my_garage = Garage()
    my_garage.cars.append("Audi")
    my_garage.cars.append("Ford")

    print(len(my_garage))


if __name__ == "__main__":
    main()