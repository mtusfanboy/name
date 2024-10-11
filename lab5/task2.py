class Circle:
    def __init__(self, radius=0):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius


circle = Circle(radius=5)
print("Изначальный радиус:", circle.get_radius())

circle.set_radius(10)

print("Новый радиус:", circle.get_radius())
