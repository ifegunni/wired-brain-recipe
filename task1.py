
"""

API DESIGN QUESTION.

Create a class called "Cmoplex" for performing arithmetic
with complex numbers. Write a driver program to test
your class.

Complex numbers have the form

reaPart + imaginaryPart * i


where j is sqrt(-1)

Use floating-point numbers to represent the data of the class. Provide a
constructor that enables an object of this class to be initialized when
it is created. The construtor should contain default values in case
no initializers are provided. The objects must support the following operations

Addition of two Complex Numbers:
    a = Complex(1,3)
    b = Complex(2,5)
    c = a + b
    print(c)

    >> 3 + 8j

Subtracting two Complex Numbers
    a = Complex(1,4)
    b = Complex(3,3)
    c = a - b

    print(c)

    >> -2 -j

Magnitude of Complex Numbers
    a = Complex(1,5)
    d = a.magnitude()
    print(d)
    >> 5.09902  # sqrt(26)

Scalar Multiplication
    (I)
    a = Complex(4,3)
    b = 2 * a
    c = a * 2

    print(b)
    >> 8 + 6j

    print(c)
    >> 8 + 6j

Scalar Division
    a = Complex(4,4)
    b = a / 2

    print(b)
    >> 2 + 2j



"""
