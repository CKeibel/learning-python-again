class Car:
    def __init__(self, make):
        self.make = make

    def __repr__(self):
        return f"<Car {self.make}>"


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Trying to add object of type '{car.__class__.__name__}' "
                            f"to list containing objects of type '{Car.__name__}'.")

        raise NotImplementedError("This method is not implemented yet.")


def main():
    my_garage = Garage()
    my_garage.add_car("Audi")
    my_garage.add_car(Car("Audi"))


if __name__ == "__main__":
    main()
