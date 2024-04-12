import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

# Пример использования:
point1 = Point(1, 2)
point2 = Point(4, 6)
print(point1.distance_to(point2))
point1.set_coordinates(3, 5)
print(point1.get_coordinates())
