def main():
    try:

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        print(f"Большее число: {max(num1, num2)}")

    except ValueError:
        print("Вы ввели не число")
    except Exception as ex_:
        print(f"Произошла ошибка во время выполнения: {ex_}")


if __name__ == "__main__":
    main()
