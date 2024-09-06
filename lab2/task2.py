def describe_person(name, age=30) -> None:
    print(f"Имя: {name}")
    print(f"Возраст: {age}")


def main():
    describe_person("Alex", 20)


if __name__ == "__main__":
    main()
