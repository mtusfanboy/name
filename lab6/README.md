# Лабораторная работа №6: Работа с классами ч.2

## Описание работы
В данной лабораторной работе рассматриваются более сложные аспекты объектно-ориентированного программирования (ООП) в Python, такие как инкапсуляция, наследование и полиморфизм. Учащиеся изучают, как защищать данные с помощью инкапсуляции, создавать иерархии классов с использованием наследования, а также переопределять методы для реализации полиморфизма. Работа включает два задания:

1. **Защита данных пользователя**: Учащиеся создают класс `UserAccount` с приватным атрибутом пароля и методами для его изменения и проверки.
2. **Полиморфизм и наследование**: Учащиеся создают базовый класс `Vehicle` и производный класс `Car`, переопределяя метод для вывода информации о транспортном средстве.

## Задание 1: Защита данных пользователя

### Реализация класса `UserAccount`
```python
class UserAccount:
    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.__password = password
        pass

    def set_password(self, new_password):
        try:
            self.__password = new_password
            if self.__password == new_password:
                return True
        except Exception:
            return False

    def check_password(self, password):
        return self.__password == password


user = UserAccount(
    username="Alex",
    email="test@test.com",
    password="Qwerty"
)


if __name__ == "__main__":
    print(user.check_password("Qwerty"))
    print(user.check_password("Qwerty1"))

    user.set_password("Qwerty1")

    print(user.check_password("Qwerty1"))
```

## Задание 2: Полиморфизм и наследование

### Реализация классов `Vehicle` и `Car`
```python
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
```

## Заключение
В ходе выполнения лабораторной работы были освоены более сложные концепции ООП в Python, такие как инкапсуляция, наследование и полиморфизм. Учащиеся научились защищать данные с помощью приватных атрибутов, создавать иерархии классов и переопределять методы для реализации полиморфного поведения.