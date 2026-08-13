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

    def test_price_setter_zero_rejected(self, capsys):
        p = Product("Phone", "Nice", 1000.0, 1)
        old_price = p.price
        p.price = 0
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert p.price == old_price

    def test_price_setter_negative_rejected(self, capsys):
        p = Product("Phone", "Nice", 1000.0, 1)
        old_price = p.price
        p.price = -100
        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert p.price == old_price

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
        cat = Category("Phones", "All phones", [])
        cat.add_product(p1)
        assert "A, 100.0 руб. Остаток: 2 шт." in cat.products

    def test_products_property_returns_string(self):
        p1 = Product("B", "Desc B", 200.0, 3)
        cat = Category("Phones", "All phones", [p1])
        assert "B, 200.0 руб. Остаток: 3 шт." in cat.products

    def test_product_count_property(self):
        p1 = Product("C", "Desc C", 300.0, 4)
        p2 = Product("D", "Desc D", 400.0, 5)
        cat = Category("Phones", "All phones", [p1, p2])
        assert cat.product_count == 2

def test_add_product_increments_class_counter():
    Category.product_count_total = 0  # сброс счётчика
    cat1 = Category("Phones", "All phones", [])
    cat2 = Category("TVs", "All TVs", [])

    p1 = Product("Phone A", "Nice phone", 1000.0, 1)
    p2 = Product("TV A", "Big TV", 2000.0, 1)

    cat1.add_product(p1)
    assert Category.get_total_product_count() == 1

    cat2.add_product(p2)
    assert Category.get_total_product_count() == 2

    # Ещё одно добавление
    cat1.add_product(Product("Phone B", "Another phone", 1500.0, 1))
    assert Category.get_total_product_count() == 3
