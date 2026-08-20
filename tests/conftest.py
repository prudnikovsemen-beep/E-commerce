import pytest
from src.category import Category

@pytest.fixture(autouse=True)
def reset_category_counter():
    """Сбрасывает глобальный счётчик перед каждым тестом."""
    Category.product_count = 0
    yield
