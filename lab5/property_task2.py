class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def rradius(self):
        return self.radius

    @rradius.setter
    def rradius(self, radius: int):
        self.radius = radius


circle = Circle(radius=5)
print("Изначальный радиус:", circle.rradius)

circle.rradius = 10

print("Новый радиус:", circle.rradius)
