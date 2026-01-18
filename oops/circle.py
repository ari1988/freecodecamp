class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self): # A getter to get radius
        return self._radius
    
    @property
    def area(self):
        return 3.14 * (self._radius ** 2)
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive.")
        self._radius = value

c1 = Circle(3)
print(c1.area)
c1.radius = 8
print(c1.radius)
print(c1.area)