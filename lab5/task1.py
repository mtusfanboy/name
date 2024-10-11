class Book:
    title: str = "Война и мир"
    author: str = "Л. Н. Толстой"
    year: int = 1869

    def get_info(self):
        return f"Название книги: {self.title}, Автор: " \
            f"{self.author}, Год издания: {self.year}"


print(Book().get_info())
