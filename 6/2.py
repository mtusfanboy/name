class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        """Возвращает информацию о транспортном средстве."""
        return f"Марка: {self.make}, Модель: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)  # Вызов конструктора базового класса
        self.fuel_type = fuel_type

    def get_info(self):
        """Переопределяем метод для включения информации о типе топлива."""
        base_info = super().get_info()
        return f"{base_info}, Тип топлива: {self.fuel_type}"


# Создаем объект класса Car
car = Car("Toyota", "Corolla", "Бензин")

# Получаем информацию о автомобиле
# Должно вывести: Марка: Toyota, Модель: Corolla, Тип топлива: Бензин
print(car.get_info())
