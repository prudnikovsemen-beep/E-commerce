import pytest
from src.product import Product
from src.category import Category


class TestCategoryMagicMethods:
    @pytest.fixture
    def category_with_products(self):
        p1 = Product("Phone", "Nice phone", 1000.0, 2)
        p2 = Product("Laptop", "Good laptop", 5000.0, 1)
        return Category("Electronics", "electronics", [p1, p2])

    def test_str_representation(self, category_with_products):
        cat = category_with_products
        # Сумма quantity: 2 + 1 = 3
        expected = "Electronics, количество продуктов: 3 шт."
        assert str(cat) == expected

    def test_len_returns_count_of_objects(self, category_with_products):
        cat = category_with_products
        # В списке 2 объекта Product
        assert len(cat) == 2

    def test_contains_checks_instance(self, category_with_products):
        cat = category_with_products
        # Берём объект, который ТОЧНО лежит внутри категории
        p1 = cat._products[0]
        p_new = Product("Tablet", "New tablet", 300.0, 5)

        # Проверяем, что тот же самый объект находится в категории
        assert p1 in cat
        # И что новый объект там не находится
        assert p_new not in cat

    def test_iteration_works(self, category_with_products):
        cat = category_with_products
        products_list = list(cat)

        assert len(products_list) == 2
        # Обращаемся к элементам списка по индексу
        assert products_list[0].name == "Phone"
        assert products_list[1].name == "Laptop"
