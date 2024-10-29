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
