import math


class Rectangle:
    """Rectangle class with width and height attributes."""
    
    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
    
    def set_width(self, width):
        """Set the width of the rectangle."""
        self.width = width
    
    def set_height(self, height):
        """Set the height of the rectangle."""
        self.height = height
    
    def get_area(self):
        """Return area (width × height)."""
        return self.width * self.height
    
    def get_perimeter(self):
        """Return perimeter 2(width + height)."""
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        """Return diagonal √(width² + height²)."""
        return math.sqrt(self.width ** 2 + self.height ** 2)
    
    def get_picture(self):
        """Return a string representation of the shape using * characters."""
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        
        return picture
    
    def get_amount_inside(self, shape):
        """Return the number of times the passed shape could fit inside this shape."""
        horizontal_fit = self.width // shape.width
        vertical_fit = self.height // shape.height
        return horizontal_fit * vertical_fit
    
    def __str__(self):
        """String representation of Rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    
    def __init__(self, side):
        """Initialize square with a single side length."""
        super().__init__(side, side)
    
    def set_width(self, side):
        """Set both width and height to the side length."""
        self.width = side
        self.height = side
    
    def set_height(self, side):
        """Set both width and height to the side length."""
        self.width = side
        self.height = side
    
    def set_side(self, side):
        """Set both width and height to the side length."""
        self.width = side
        self.height = side
    
    def __str__(self):
        """String representation of Square."""
        return f"Square(side={self.width})"


# Test the implementation
if __name__ == "__main__":
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))
