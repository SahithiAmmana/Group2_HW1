from ..code import calculator as calc

def test_add():  
    a = 5
    b = 6
    c = calc.addition(a,b)
    assert c == 11, "Addition test case is passed"

def test_sub():
    a = 7
    b = 8
    c = calc.subtraction(a,b)
    assert c == -1, "Substraction test case id passed"

def test_mul():
    a = 9
    b = 3
    c = calc.multiplication(a,b)
    assert c == 27, "Multiplication test case is passed"

def test_div():
    a = 8
    b = 2
    c = calc.division(a,b)
    assert c == 4, "Division test case is passed"

def test_div_zero():
    a = 7
    b = 0
    c = calc.division(a,b)
    assert c == "Enter non-zero divisor", "Division by zero test case is passed"