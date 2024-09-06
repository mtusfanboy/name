def main():
    try:
        number = int(input("Введите число: "))
        if number <= 0:
            print("Ничего не будет выведено, если введеное число меньше 1")
            return
        for i in range(1, int(number) + 1):
            print(i)
    except ValueError:
        print("Нужно ввести целое число")
    except Exception as ex_:
        print(f"Произошла ошибка во время выполнения: {ex_}")


if __name__ == "__main__":
    main()
