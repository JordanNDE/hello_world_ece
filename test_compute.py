from compute import add, subtract

def test_add():
    assert add(2,3) == 5

def test_add_null():
    assert add(0,0) == 0

def test_subtract():
    assert subtract(2,3) == -1
    