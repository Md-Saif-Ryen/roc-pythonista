class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getarea(self):
        return (22 / 7) * (self.radius) ** 2

    def getparameter(self):
        return 2 * (22 / 7) * self.radius
