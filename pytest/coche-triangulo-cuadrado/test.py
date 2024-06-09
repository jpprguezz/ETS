import pytest
from tarea import Car, Triangle, Square

@pytest.fixture
def car() -> Car:
    return Car('Ford', 'Explorer', 'Brown')

@pytest.fixture
def triangle() -> Triangle:
    return Triangle(5, 10)

@pytest.fixture
def square() -> Square:
    return Square(10)

def test_car_engine(car: Car):
    assert not car.engine_status
    car.toggle_engine()
    assert car.engine_status

def test_triangle_area(triangle: Triangle):
    assert triangle.area == 25

def test_square_perimeter(square: Square):
    assert square.perimeter == 40