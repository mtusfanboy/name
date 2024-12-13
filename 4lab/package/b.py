import random


def cool_sort(arr=None):
    if not arr:
        arr = []
        for i in range(random.randint(5, 25)):
            arr.append(random.randint(-1000, 1000))

    while sorted(arr) != arr:
        random.shuffle(arr)
    return arr
