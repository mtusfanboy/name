def is_prime(number) -> bool:
    if not isinstance(number, int):
        return False
    if number <= 1:
        return False
    if number <= 3:
        return True

    divs = set()

    for i in range(1, int(number**0.5) + 1):
        if number % i == 0:
            divs.add(i)
            divs.add(number // i)

    return (sorted(divs)) == [1, number]


def main():
    print(is_prime(7))


if __name__ == "__main__":
    main()
