class Rational:

    def __init__(self, num = 0, denum = 1):
        self.num = num
        self.denum = denum

    def __str__(self):
        return(str(int(self.num)) + "/" + str(int(self.denum)) if self.denum != 1 else str(int(self.num)))

    def __add__(self, other):
        lower_operation = self.denum * other.denum
        upper_operation = (self.num * (lower_operation / self.denum)) + (other.num * (lower_operation / other.denum))
        for i in range(2, 10):
            while lower_operation % i == 0 and upper_operation % i == 0:
                lower_operation /= i
                upper_operation /= i
        return Rational(upper_operation, lower_operation)


    def __sub__(self, other):
        lower_operation = self.denum * other.denum
        upper_operation = (self.num * (lower_operation / self.denum)) - (other.num * (lower_operation / other.denum))
        for i in range(2, 10):
            while lower_operation % i == 0 and upper_operation % i == 0:
                lower_operation /= i
                upper_operation /= i
        return Rational(upper_operation, lower_operation)

    def __mul__(self, other):
        lower_operation = self.denum * other.denum
        upper_operation = self.num * other.num
        for i in range(2, 10):
            while lower_operation % i == 0 and upper_operation % i == 0:
                lower_operation /= i
                upper_operation /= i
        return Rational(upper_operation, lower_operation)

    def __truediv__(self, other):
        other.num, other.denum = other.denum, other.num
        return self * other

    def asFloat(self):
        return float(self.num / self.denum)


def main():
    print("#"*10 +  "Test result" + "#"*10)
    print("#"*10 +  "Test Addition" + "#"*10)
    test_addition()
    print()
    print("#"*10 +  "Test Subtraction" + "#"*10)
    test_subtraction()
    print()
    print("#"*10 +  "Test Multiplication" + "#"*10)
    test_multiplication()
    print()
    print("#"*10 +  "Test Division" + "#"*10)
    test_division()
    print()
    print("#"*10 +  "Test as Float" + "#"*10)
    test_asFloat()

def test_addition():
    a = Rational(1, 13)
    b = Rational(12, 13)
    result = a + b
    print(result)
    try:
        assert(result.num == 1 and result.denum == 13)
        print("PASSED!!!")
    except:
        raise TypeError("Wrong input")

def test_subtraction():
    a = Rational(1, 4)
    b = Rational(3, 4)
    result = a - b
    print(result)

    try:
        assert(result.num == -1 and result.denum == 2)
        print("PASSED!!!")
    except:
        raise valueError("Wrong input")

def test_multiplication():
    a = Rational(1, 4)
    b = Rational(2, 5)
    result = a * b
    print(result)
    try:
        assert(result.num == 1 and result.denum == 10)
        print("PASSED!!!")
    except:
        raise valueError("Wrong input")

def test_division():
    a = Rational(2,3)
    b = Rational(4, 5)
    result = a / b
    print(result)
    # try:
    assert(result.num == 5 and result.denum == 6)
    print("test_division PASSED!!!")
    # except:
        # raise valueError("Wrong input")

def test_asFloat():
    a = Rational(1, 2)
    result = a.asFloat()
    print(result)
    print("PASSED!!!")


if __name__ == "__main__":
    main()
