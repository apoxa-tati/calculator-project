def add(a: float, b: float) -> float:
    """
    Сложение двух чисел.

    Args:
        a: Первое число
        b: Второе число

    Returns:
        Сумма a и b
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Вычитание двух чисел.

    Args:
        a: Уменьшаемое
        b: Вычитаемое

    Returns:
        Разность a и b
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """
    Умножение двух чисел.

    Args:
        a: Первый множитель
        b: Второй множитель

    Returns:
        Произведение a и b
    """
    return a * b


def divide(a: float, b: float) -> float:
    """
    Деление двух чисел.

    Args:
        a: Делимое
        b: Делитель

    Returns:
        Частное a и b

    Raises:
        ValueError: Если делитель равен 0
    """
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b
