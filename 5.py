class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"Book title: {self.title}, Author: {self.author}, Year: {self.year}"


book = Book("Clean Code", "Robert Martin", 2008)
print(book.get_info())


class Circle:
    def __init__(self, radius):
        print(f"radius is {radius}")
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius):
        print(f"radius changed to {new_radius}")
        self._radius = new_radius

    @radius.deleter
    def radius(self):
        print(f"del radius ({self.radius})")
        del self._radius


circle = Circle(5)
circle.radius = 10
print(circle.radius)
del circle.radius
