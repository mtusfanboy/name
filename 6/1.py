class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # Приватный атрибут пароля

    def set_password(self, new_password):
        """Изменяет пароль аккаунта."""
        self.__password = new_password

    def check_password(self, password):
        """Проверяет, соответствует ли введённый пароль текущему паролю."""
        return self.__password == password


# Создаем объект класса UserAccount
user = UserAccount("user1", "user1@example.com", "initialPassword")

print(user._UserAccount__password)
# average python encapsulation🤓
# Изменяем пароль
user.set_password("newSecurePassword")

# Проверяем новый пароль
is_correct = user.check_password("newSecurePassword")
# Должно вывести: Пароль корректен: True
print(f"Пароль корректен: {is_correct}")

# Проверяем неправильный пароль
is_correct = user.check_password("wrongPassword")
# Должно вывести: Пароль корректен: False
print(f"Пароль корректен: {is_correct}")
