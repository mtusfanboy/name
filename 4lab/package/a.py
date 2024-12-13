def good_night(n=42):
    if n == 1:
        return 2
    if n == 2:
        return 3
    else:
        return good_night(n-1) + good_night(n-2)

# print(good_night(42))
