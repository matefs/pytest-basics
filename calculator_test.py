from calculator import sum

def test_sum():
    result = sum(1,2)
    assert result == 3

def test_sum2():
    result = sum(1,1)
    assert result == 2

def test_sum3():
    result = sum(1,3)
    assert result == 4
