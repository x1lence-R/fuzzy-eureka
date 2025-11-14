import pytest

# Тест 1: Проверка математических операций
def test_addition():
    """Тест сложения чисел"""
    assert 2 + 2 == 4
    assert 10 + 5 == 15
    assert -1 + 1 == 0
    print("Тест сложения пройден успешно")

# Тест 2: Проверка работы со строками
def test_string_operations():
    """Тест операций со строками"""
    text = "GitHub Actions"
    
    # Проверка длины строки
    assert len(text) == 14
    
    # Проверка содержания подстроки
    assert "GitHub" in text
    
    # Проверка метода upper()
    assert text.upper() == "GITHUB ACTIONS"
    
    # Проверка метода split()
    words = text.split()
    assert len(words) == 2
    assert words[0] == "GitHub"
    
    print("Тест операций со строками пройден успешно")

# Дополнительный тест 3: Проверка работы со списками (бонус)
def test_list_operations():
    """Тест операций со списками"""
    numbers = [1, 2, 3, 4, 5]
    
    # Проверка длины списка
    assert len(numbers) == 5
    
    # Проверка суммы элементов
    assert sum(numbers) == 15
    
    # Проверка максимального элемента
    assert max(numbers) == 5
    
    # Проверка минимального элемента
    assert min(numbers) == 1
    
    print("Тест операций со списками пройден успешно")

# Тест 4: Проверка с использованием исключений
def test_division():
    """Тест деления и обработки ошибок"""
    # Нормальное деление
    assert 10 / 2 == 5
    
    # Проверка деления на ноль
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0
    
    print("Тест деления пройден успешно")
