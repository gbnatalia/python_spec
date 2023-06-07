import pytest
from matrix import Matrix

@pytest.fixture
def data():
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m3 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    m4 = Matrix([[1, 2], [4, 5], [7, 8]])
    return [m1, m2, m3, m4]

def test_equal(data):
    assert (data[0] == data[1]) == True, 'Грустно!'
    assert (data[0] == data[2]) == False, 'Грустно!'

def test_not_equal(data):
    assert (data[0] != data[1]) == False, 'Грустно!'
    assert (data[0] != data[2]) == True, 'Грустно!'

def test_lt(data):
    assert (data[0] < data[1]) == False, 'Грустно!'

def test_le(data):
    assert (data[0] <= data[1]) == True, 'Грустно!'

def test_gt(data):
    assert (data[0] > data[1]) == False, 'Грустно!'

def test_ge(data):
    assert (data[0] >= data[1]) == True, 'Грустно!'

def test_add(data):
    assert (data[0] + data[1]) == Matrix([[2, 4, 6], [8, 10, 12], [14, 16, 18]]), 'Грустно!'

def test_transport(data):
    assert data[3].transpose() == Matrix([[1, 4, 7], [2, 5, 8]]), 'Грустно!'

if __name__=="__main__":
    pytest.main()






