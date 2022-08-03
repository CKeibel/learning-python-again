class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    """
    class method, to get wanted formatting of children etc. 
    works like staticmethod but with more functionality because of 'cls'.
    """
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

    def __repr__(self):
        return f"<FixedFloat {self.amount:.2f}>"


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.sign = "Euro"

    def __repr__(self):
        return f"<Euro {self.amount:.2f} {self.sign}>"


def main():
    n = FixedFloat.from_sum(2.43532, 0.5213)
    print(n)

    x = Euro.from_sum(2.5, 3.2)
    print(x)


if __name__ == "__main__":
    main()
