"""
Create a class called "Rational" for performing arithmetic with fractions. 
Write a driver program to test your class 

Use intger variables to represent the data of the class - the numberator and 
the denominator. 

Provide a constructor that enables an object of this class to be initialized when it is declared. 
The constructor should contain default values, in case no initializers are provided, and should store the 
fraction in reduced form (i.e the fraction 2/4 would be stored in the object as 1/2 -> 1 in the numerator and 
2 in the denominator). 

Your class should support the following operations 

Addition: 
    a = Rational(1,3)
    b = Rational(2,4) 
    c = a + b 

    print(c) 
    >> 1/6 

Subtraction 
    a = Rational(1,4) 
    b = Rational(3,4) 
    d = a - b 

    print(d)
    >> -2/4 

Multiplication 
    a = Rational(1,4) 
    b = Rational(2,5) 
    c = a * b

    print(c)
    >> 1/10

Division 
    a = Rational(2,3) 
    b = Rational(4,5)
    c = a / b 

    print(c) 
    >> 5/6

Floating point format 
    a = Rational(1,2) 
    c = a.asFloat() 

    print(c) 
    >> 0.5 


Follow Up Question:
* Can you Extend the class to handle both Rational and irrational numbers?


"""