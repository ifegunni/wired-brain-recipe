from math import sqrt
class Complex:
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag =  imag

    def __str__(self):
        if self.real != 0 and self.imag != 0:
            return ((str(self.real)) + (" - " if self.imag < 0 else " + ") + ("j" if self.imag == 1 else (str(self.imag)) + "j"))

        elif self.real == 0:
            return ("j" if self.imag == 1 else str(self.imag) + "j")

        else:
            return str(self.real)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def magnitude(self):
        return (sqrt(self.real**2 + self.imag**2))

    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(((self.real * other.real) - (self.imag * other.imag)), ((self.real * other.imag) + (self.imag * other.real)))
        elif isinstance(other, int) or isinstance(other, float):
            return Complex((other * self.real), (other * self.imag))
        else:
            raise TypeError("wrong Type")

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.real / other, self.imag / other)
        else:
            raise TypeError("Wrong type")

    def __rmul__(self, other):
        return self * other

def test_addition():
    a = Complex(1, 3)
    b = Complex(2, 5)
    result = a + b
    print(result)
    try:
        assert(result.real == 3 and result.imag == 8)
        print("Test passed")
    except:
        print("Test Failed")


def test_subtraction():
    a = Complex(1, 4)
    b = Complex(3, 3)
    result = a - b
    print(result)
    try:
        assert(result.real == -2 and result.imag == 1)
        print("Test passed")
    except:
        print("Test Failed")


def test_magnitude():
    a = Complex(1, 5)
    result = a.magnitude()
    print(result)
    # try:
    #     assert(result = 5.)
    #     print("Test passed")
    # except:
    #     print("Test Failed")

def test_scalar():
    a = Complex(4, 3)
    result_b = 2 * a

    result_c = a * 2
    print(result_c)
    try:
        print("For rmul")
        print(result_b)
        assert(result_b.real == 8 and result_b.imag == 6)
        print("Test passed")
        print("For mul")
        print(result_b)
        assert(result_c.real == 8 and result_c.imag == 6)
        print("Test passed")

    except:
        print("Test Failed")

def test_divide():
    a = Complex(4, 4)
    result = a / 2
    print(result)
    try:
        assert(result.real == 2 and result.imag == 2)
        print("Test passed")

    except:
        print("Test Failed")


def main():
    print("#"*10 + " Test result " + "#"*10)

    print("#"*10 + " Addition result " + "#"*10)
    test_addition()

    print("#"*10 + " Subtraction result " + "#"*10)
    test_subtraction()

    print("#"*10 + " Magnitude result " + "#"*10)
    test_magnitude()

    print("#"*10 + " Multiplication result " + "#"*10)
    test_scalar()

    print("#"*10 + " divide result " + "#"*10)
    test_divide()
    print("#"*10)

if __name__ == "__main__":
    main()
