class Square:
    def __init__(self, side):
        self.side = side

class Circle:
    def __init__(self, radius):
        self.radius = radius

class circleSquare(Square, Circle):
    def __init__(self, side):
        super().__init__(side)
        Circle.__init__(self, side / 2)

square_with_circle = circleSquare(4)
print(f"Сторона квадрата: {square_with_circle.side}")
print(f"Радиус окружности: {square_with_circle.radius}")