from calculator import sum

def test_sum():
    result = sum(1,2)
    assert result == 3

def test_sum2():
    result = sum(1,1)
    assert result == 2
