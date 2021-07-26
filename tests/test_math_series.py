from math_series import __version__
from math_series.series import  fibonacci,lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci():
    expected = 0
    actual =  fibonacci(0)
    assert actual == expected

def test_fibonacci2():
    expected = 1
    actual =  fibonacci(1)
    assert actual == expected

def test_fibonacci3():
    expected = 1
    actual = fibonacci(2)
    assert actual == expected
    
def test_fibonacci5():
    expected = 13
    actual = fibonacci(7)
    assert actual == expected


def test_lucas():
    expected = 2
    actual = lucas(0)
    assert actual == expected

def test_lucas():
    expected = 0
    actual = lucas(1)
    assert actual == expected    

def test_lucas():
    expected = 3
    actual = lucas(2)
    assert actual == expected    

def test_lucas():
    expected = 29
    actual = lucas(7)
    assert actual == expected

def test_sum_series():
    expected = 13
    actual = sum_series(7,0,1)
    assert actual == expected

def test_sum_series1():
    expected=0
    actual=sum_series(0)
    assert actual==expected    

   