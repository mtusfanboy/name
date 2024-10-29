class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model
        pass

    def get_info(self):
        return f"Марка: {self.make}\nМодель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type) -> None:
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return super().get_info() + f"\nТип топлива: {self.fuel_type}"


if __name__ == "__main__":
    car = Car("BMW", "7", "Бензин")
    print(car.get_info())
