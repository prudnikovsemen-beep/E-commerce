# tests/test_product_category.py
import pytest
from src.product import Product
from src.category import Category


class TestProduct:
    def test_product_creation(self):
        p = Product("Test Phone", "Good phone", 1000.0, 5)
        assert p.name == "Test Phone"
        assert p.description == "Good phone"
        assert p.price == 1000.0
        assert p.quantity == 5

    def test_price_setter_valid(self):
        p = Product("Phone", "Nice", 1000.0, 1)
        p.price = 2000.0
        assert p.price == 2000.0

    def test_price_setter_zero_rejected(self):
        p = Product("Phone", "Nice", 1000.0, 1)
        with pytest.raises(ValueError, match="Цена не может быть нулевой или отрицательной"):
            p.price = 0

    def test_price_setter_negative_rejected(self):
        p = Product("Phone", "Nice", 1000.0, 1)
        with pytest.raises(ValueError, match="Цена не может быть нулевой или отрицательной"):
            p.price = -100

    def test_new_product_class_method(self):
        data: dict[str, float | int | str] = {
            "name": "New Phone",
            "description": "Brand new",
            "price": 1500.0,
            "quantity": 3,
        }
        p = Product.new_product(data)
        assert isinstance(p, Product)
        assert p.name == "New Phone"
        assert p.description == "Brand new"
        assert p.price == 1500.0
        assert p.quantity == 3


class TestCategory:
    def test_add_product_to_category(self):
        p1 = Product("A", "Desc A", 100.0, 2)
        # Конструктор теперь: (name, description, products)
        cat = Category("Phones", "All phones", [])
        cat.add_product(p1)

        # products — это список объектов Product, а не строк
        assert len(cat.products) == 1
        assert cat.products[0] is p1

    def test_products_property_returns_objects(self):
        p1 = Product("B", "Desc B", 200.0, 3)
        cat = Category("Phones", "All phones", [p1])

        assert len(cat.products) == 1
        assert cat.products[0] is p1
        # Если хочешь проверить строковое представление, используй str(p1), но не сравнивай с жёсткой строкой
        assert cat.products[0].name == "B"

    def test_product_count_property(self):
        p1 = Product("C", "Desc C", 300.0, 4)
        p2 = Product("D", "Desc D", 400.0, 5)
        cat = Category("Phones", "All phones", [p1, p2])
        # product_count — это property, который возвращает len(_products)
        assert cat.product_count == 2


def test_add_product_increments_class_counter():
    # Сбрасываем счётчик перед тестом — это гарантирует независимость
    Category.total_product_count = 0

    category = Category("Test Category", "Test description", [])
    product = Product("Test Product", "Description", 100.0, 5)
    category.add_product(product)

    assert Category.get_total_product_count() == 1
