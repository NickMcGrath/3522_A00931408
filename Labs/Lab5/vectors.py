import math
import numbers


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

    @staticmethod
    def get_mag(a):
        """
        Static method to return the magnitude at a coordinate.
        :param a: a Vector object
        :return: the magnitude of the vector opject
        """
        return math.sqrt(a.x ** 2 + a.y ** 2 + a.z ** 2)

    def __getitem__(self, item):
        """Returns the value corresponding to the value given."""
        if item.lower() == 'x':
            return self.x
        elif item.lower() == 'y':
            return self.y
        elif item.lower() == 'z':
            return self.z

    def __setitem__(self, key, value):
        """Sets the corresponding key to value given."""
        if key.lower() == 'x':
            self.x = value
        elif key.lower() == 'y':
            self.y = value
        elif key.lower() == 'z':
            self.z = value

    def __add__(self, b):
        """Overload the + operator."""
        return Vector(b.x + self.x, b.y + self.y, b.z + self.z)

    def __sub__(self, b):
        """Overload the - operator."""
        return Vector(self.x - b.x, self.y - b.y, self.z - b.z)

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
        if isinstance(b, numbers.Number):
            return Vector(b * self.x, b * self.y, b * self.z)
        else:
            return Vector((self.y * b.z - self.z * b.y),
                          (self.z * b.x - self.x * b.z),
                          (self.x * b.y - self.y * b.x))

    def __abs__(self):
        """Overload the abs operator."""
        return abs(self.get_mag(self))

    def __isub__(self, b):
        """Overload the -= operator."""
        self.x -= b.x
        self.y -= b.y
        self.z -= b.z
        return self

    def __iadd__(self, b):
        """Overload the += operator."""
        self.x += b.x
        self.y += b.y
        self.z += b.z
        return self

    def __rmul__(self, b):
        """Overload the right * operator."""
        self.__imul__(b)

    def __imul__(self, b):
        """Overload the *= operator."""
        if isinstance(b, numbers.Number):
            self.x *= b
            self.y *= b
            self.z *= b
            return self
        else:
            return Vector((self.y * b.z - self.z * b.y),
                          (self.z * b.x - self.x * b.z),
                          (self.x * b.y - self.y * b.x))

    def __str__(self):
        """Returns a string representation of the Vector"""
        return f'Vector coordinates: x: {self.x}, y: {self.y}, z: {self.z}'


def main():
    """Testes operator functions."""
    my_vector = Vector(34, 56, 27)
    your_vector = Vector(25, 58, 30)
    print(my_vector - your_vector)
    print(my_vector + your_vector)
    print(my_vector * your_vector)
    print('multi time!')
    print(my_vector)
    print(2 * my_vector)
    print(my_vector > your_vector)
    print(my_vector >= your_vector)
    print(my_vector <= your_vector)
    print(my_vector == your_vector)
    print(my_vector != your_vector)
    my_vector += your_vector
    print(my_vector)
    my_vector *= your_vector
    print(my_vector)
    my_vector -= your_vector
    print(my_vector)
    my_vector *= 2
    print(my_vector)


if __name__ == '__main__':
    main()
