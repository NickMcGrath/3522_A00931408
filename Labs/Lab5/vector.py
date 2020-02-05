import math


class Vector:
    """Vector represents a Vector with coordinates in a 3D space."""

    def __init__(self, x, y, z):
        """
        Initialize the vector with all coordinates.
        :param x: x coordinate
        :param y: y coordinate
        :param z: z coordinate
        """
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, item):
        """Returns the value corresponding to the value given."""
        if item.lower() == 'x':
            return self.x
        elif item.lower() == 'y':
            return self.y
        elif item.lower() == 'z':
            return self.z

    @staticmethod
    def get_mag(a):
        """Static method to return the magnitude at a coordinate."""
        return math.sqrt(a.x ** 2 + a.y ** 2 + a.z ** 2)

    def __add__(self, b):
        """Overload the + operator."""
        return Vector(b.x + self.x, b.y + self.y, b.z + self.z)

    def __lt__(self, b):
        """Overload the < operator."""
        return self.get_mag(self) < self.get_mag(b)

    def __gt__(self, b):
        """Overload the > operator."""
        return self.get_mag(self) > self.get_mag(b)

    def __le__(self, b):
        """Overload the <= operator."""
        return self.get_mag(self) <= self.get_mag(b)

    def __ge__(self, b):
        """Overload the >= operator."""
        return self.get_mag(self) >= self.get_mag(b)

    def __eq__(self, b):
        """Overload the == operator."""
        return self.get_mag(self) == self.get_mag(b)

    def __ne__(self, b):
        """Overload the != operator."""
        return self.get_mag(self) != self.get_mag(b)

    def __mul__(self, b):
        """Overload the * operator."""
        return Vector(b * self.x, b * self.y, b * self.z)

    def __abs__(self):
        """Overload the abs operator."""
        return abs(self.get_mag(self))

    def __isub__(self, b):
        """Overload the -= operator."""
        self.x -= b.x
        self.y -= b.y
        self.z -= b.z

    def __iadd__(self, b):
        """Overload the += operator."""
        self.x += b.x
        self.y += b.y
        self.z += b.z

    def __imul__(self, b):
        """Overload the *= operator."""
        self.x *= b
        self.y *= b
        self.z *= b

    def __str__(self):
        """Returns a string representation of the project"""
        return f'x: {self.x}, y: {self.y}, z: {self.z}'
