import pytest
from main import Product, Category


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
        old_price = p.price
        p.price = 0
        # Цена не должна измениться
        assert p.price == old_price

    def test_price_setter_negative_rejected(self):
        p = Product("Phone", "Nice", 1000.0, 1)
        old_price = p.price
        p.price = -100
        assert p.price == old_price

    def test_new_product_class_method(self):
        data = {
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
    def test_category_creation_with_products(self):
        p1 = Product("A", "Desc A", 100.0, 2)
        p2 = Product("B", "Desc B", 200.0, 3)
        cat = Category("Phones", "All phones", [p1, p2])
        # Убеждаемся, что products доступен через property
        products = cat.products
        assert len(products) == 2
        assert products[0] is p1
        assert products[1] is p2

    def test_add_product_to_category(self):
        p1 = Product("A", "Desc A", 100.0, 2)
        cat = Category("Phones", "All phones", [])
        cat.add_product(p1)
        products = cat.products
        assert len(products) == 1
        assert products[0] is p1

    def test_products_property_returns_string_representation(self):
        p1 = Product("A", "Desc A", 100.0, 2)
        cat = Category("Phones", "All phones", [p1])
        result = cat.products  # это строка по заданию
        assert "A, 100.0 руб. Остаток: 2 шт." in result

    def test_product_count_property(self):
        p1 = Product("A", "Desc A", 100.0, 2)
        p2 = Product("B", "Desc B", 200.0, 3)
        cat = Category("Phones", "All phones", [p1, p2])
        assert cat.product_count == 2
