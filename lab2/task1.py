def greet(name) -> None:
    print(f"Hello, {name}!")


def square(number) -> int | float | None:
    if isinstance(number, (int, float)):
        return number ** 2
    else:
        print("Вы передали не число!")
        return None


def max_of_two(x, y) -> int | float | None:
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        return max(x, y)
    else:
        print("Функция принимает только числа")
        return None


def main():
    greet("Alex")
    print(square(5))
    print(max_of_two(1, 2))


if __name__ == "__main__":
    main()
