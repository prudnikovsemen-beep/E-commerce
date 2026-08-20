import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def sample_product() -> Product:
    return Product(
        name="Test Product",
        description="Описание товара",
        price=100.0,
        quantity=5,
    )


@pytest.fixture
def sample_category() -> Category:
    cat = Category("Electronics", "electronics")
    cat.add_product(Product("Phone", "Смартфон", 200.0, 2))
    cat.add_product(Product("Tablet", "Планшет", 300.0, 1))
    return cat


@pytest.fixture(autouse=True)
def reset_category_counter():
    """Сбрасывает глобальный счётчик товаров перед каждым тестом."""
    Category.total_products_count = 0
    yield
