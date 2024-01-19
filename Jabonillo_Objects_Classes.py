import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Compute and print the area of the circle."""
        circle_area = math.pi * self.radius**2
        print(f"Area of the circle with radius {self.radius}: {circle_area:.2f}")

    def perimeter(self):
        """Compute and print the perimeter of the circle."""
        circle_perimeter = 2 * math.pi * self.radius
        print(f"Perimeter of the circle with radius {self.radius}: {circle_perimeter:.2f}")

# Example usage:
radius_value = 5
my_circle = Circle(radius_value)

my_circle.area()
my_circle.perimeter()
