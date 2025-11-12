from calculator import add, divide, multiply, subtract
import pytest


def test_add():
    """Тестирование функции сложения"""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(2.5, 3.5) == 6.0


def test_subtract():
    """Тестирование функции вычитания"""
    assert subtract(5, 3) == 2
    assert subtract(0, 10) == -10
    assert subtract(10, 10) == 0
    assert subtract(-5, -3) == -2


def test_multiply():
    """Тестирование функции умножения"""
    assert multiply(2, 5) == 10
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0
    assert multiply(2.5, 4) == 10.0


def test_divide():
    """Тестирование функции деления"""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5
    assert divide(-10, 2) == -5


def test_divide_by_zero():
    """Тестирование деления на ноль"""
    with pytest.raises(ValueError) as exc_info:
        divide(5, 0)
    assert "Деление на ноль невозможно" in str(exc_info.value)


def test_divide_by_zero_message():
    """Тестирование сообщения об ошибке при делении на ноль"""
    with pytest.raises(ValueError, match="Деление на ноль невозможно"):
        divide(10, 0)
