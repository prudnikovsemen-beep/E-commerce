import pytest
from src.product import Product
from src.category import Category
import subprocess
import os


class TestProduct:
    """Тесты для класса Product (инициализация, свойства, валидация цены)"""

    def test_product_creation(self):
        p = Product("iPhone 15", "128GB, Black", 999.99, 10)
        assert p.name == "iPhone 15"
        assert p.quantity == 10

    def test_price_setter_valid(self):
        p = Product("Test", "desc", 100.0, 5)
        p.price = 200.0
        assert p.price == 200.0

    def test_price_setter_zero_rejected(self, capsys):
        """Тест ожидает, что при цене 0 будет напечатано сообщение в консоль"""
        p = Product("Test", "desc", 100.0, 5)
        p.price = 0  # Это вызовет print внутри сеттера

        captured = capsys.readouterr()
        # Проверяем, что в stdout есть нужная фраза
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        # Цена не должна измениться
        assert p.price == 100.0

    def test_price_setter_negative_rejected(self):
        p = Product("Test", "desc", 100.0, 5)
        with pytest.raises(ValueError, match="Цена не может быть отрицательной"):
            p.price = -100

    @classmethod
    def test_new_product_class_method(cls):
        data = {"name": "Samsung TV", "description": "4K, 55 дюймов", "price": 45000.0, "quantity": 3}
        p = Product.new_product(data)
        assert p.name == "Samsung TV"
        assert p.price == 45000.0


class TestCategory:
    """Тесты для класса Category (добавление товаров, счётчики)"""

    def test_add_product_to_category(self):
        cat = Category("Электроника", "Товары для дома")
        p = Product("Наушники", "Беспроводные", 5000.0, 2)
        cat.add_product(p)

        products = cat.get_products_objects()
        assert len(products) == 1
        assert products[0].name == "Наушники"

    def test_products_property_returns_string(self):
        cat = Category("Смартфоны", "Описание")
        p = Product("Xiaomi", "128GB", 30000.0, 1)
        cat.add_product(p)

        # Свойство products возвращает список строк (вызовов __str__)
        result = cat.products
        assert isinstance(result, list)
        assert len(result) == 1
        assert "Xiaomi" in result[0]

    def test_product_count_property(self):
        cat = Category("Ноутбуки", "Описание")
        cat.add_product(Product("MacBook", "M1", 150000.0, 1))
        cat.add_product(Product("Dell", "i5", 80000.0, 2))
        assert cat.product_count == 2

    def test_add_product_increments_class_counter(self):
        # Сбрасываем счётчик в 0 перед тестом — это критически важно!
        Category._total_product_count = 0

        cat = Category("Тест категория", "Описание", products=[])
        assert Category.get_total_product_count() == 0

        p = Product("Товар для теста", "Desc", 100.0, 1)
        cat.add_product(p)

        assert Category.get_total_product_count() == 1


class TestProductStr:
    """Тесты для Product.__str__"""

    def test_str_format_basic(self):
        p = Product("Samsung Galaxy S23 Ultra", "256GB, Серый", 180000.0, 5)
        s = str(p)
        assert s == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

    def test_str_with_different_values(self):
        p = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        s = str(p)
        assert s == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


class TestCategoryStr:
    """Тесты для Category.__str__ (с подсчётом общего количества товаров)"""

    def test_str_total_quantity_sum(self):
        p1 = Product("A", "desc A", 100.0, 2)
        p2 = Product("B", "desc B", 200.0, 3)
        cat = Category("Смартфоны", "Описание", [p1, p2])
        s = str(cat)
        assert s == "Смартфоны, количество продуктов: 5 шт."

    def test_str_empty_products(self):
        cat = Category("Пустая категория", "Нет товаров", [])
        s = str(cat)
        assert s == "Пустая категория, количество продуктов: 0 шт."


class TestProductAdd:
    """Тесты для Product.__add__: сумма (цена * количество)"""

    def test_add_returns_total_cost(self):
        a = Product("Товар A", "desc", 100.0, 10)
        b = Product("Товар B", "desc", 200.0, 2)
        total = a + b
        assert total == 1400.0

    def test_add_order_independence(self):
        a = Product("Товар A", "desc", 100.0, 10)
        b = Product("Товар B", "desc", 200.0, 2)
        assert (a + b) == (b + a)

    def test_add_with_zero_quantity(self):
        a = Product("Товар A", "desc", 100.0, 0)
        b = Product("Товар B", "desc", 200.0, 2)
        total = a + b
        assert total == 400.0


def test_main_py_runs_without_errors():
    """Проверка, что main.py запускается без ошибок"""
    result = subprocess.run(
        ["python", "main.py"],
        cwd=os.getcwd(),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"main.py завершился с ошибкой:\n{result.stderr}"
