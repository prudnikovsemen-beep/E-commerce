import pytest
from src.models import Product, Category


class TestProduct:
    def test_product_initialization(self):
        p = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
        assert p.name == "Samsung Galaxy S23 Ultra"
        assert p.description == "256GB, Серый"
        assert p.price == 180000.0
        assert p.quantity == 5

    def test_product_types(self):
        p = Product("Phone", "Good phone", 999.99, 10)
        assert isinstance(p.name, str)
        assert isinstance(p.description, str)
        assert isinstance(p.price, (int, float))
        assert isinstance(p.quantity, int)


class TestCategory:
    @pytest.fixture
    def products(self):
        return [
            Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5),
            Product("Iphone 15", "512GB", 210000.0, 8),
        ]

    def test_category_initialization(self, products):
        cat = Category("Смартфоны", "Описание категории", products)
        assert cat.name == "Смартфоны"
        assert cat.description == "Описание категории"
        assert cat.products == products

    def test_category_products_list_contains_product_objects(self, products):
        cat = Category("Смартфоны", "Описание", products)
        for p in cat.products:
            assert isinstance(p, Product)

    def test_category_count_increases_on_creation(self):
        Category.category_count = 0
        Category.product_count = 0

        c1 = Category("Смартфоны", "Описание 1", [])
        c2 = Category("Телевизоры", "Описание 2", [])

        assert Category.category_count == 2
        assert c1.category_count == 2
        assert c2.category_count == 2

    def test_product_count_increases_by_number_of_products_in_category(self):
        Category.category_count = 0
        Category.product_count = 0

        p1 = Product("P1", "D1", 100.0, 1)
        p2 = Product("P2", "D2", 200.0, 2)
        p3 = Product("P3", "D3", 300.0, 3)

        Category("C1", "Desc", [p1, p2])
        Category("C2", "Desc", [p3])

        assert Category.product_count == 3


def test_category_get_total_price():
    p1 = Product("Товар 1", "Описание", 100.0, 2)  # 200 ₽
    p2 = Product("Товар 2", "Описание", 200.0, 3)  # 600 ₽
    cat = Category("Электроника", "Товары", [p1, p2])

    assert cat.get_total_price() == 800.0
