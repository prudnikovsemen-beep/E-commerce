import pytest
from src.product import Product, BaseProduct
from src.smartphone import Smartphone


class TestBaseProduct:
    def test_base_product_cannot_be_instantiated(self):
        """Абстрактный базовый класс нельзя создать напрямую"""
        with pytest.raises(TypeError):
            BaseProduct("Name", "Desc", 100.0, 5)

    def test_product_is_instance_of_base(self):
        """Обычный продукт является экземпляром базового класса"""
        p = Product("Test", "Desc", 100.0, 5)
        assert isinstance(p, BaseProduct)


class TestLoggingMixin:
    def test_logging_mixin_prints_creation(self, capsys):
        """При создании Product в stdout должно появиться сообщение о создании"""
        # Создаем объект — в этот момент сработает __init__ миксина и сделает print
        Product("Test", "Desc", 100.0, 5)

        captured = capsys.readouterr()

        # Проверяем, что вывод не пустой и содержит нужные подстроки
        assert captured.out != ""
        assert "Product(" in captured.out
        assert "Test" in captured.out

    def test_subclasses_also_print_creation(self, capsys):
        """Подклассы (например, Smartphone) тоже должны печатать сообщение через миксин"""
        Smartphone(
            "Galaxy",
            "256GB",
            180000.0,
            5,
            0.9,  # efficiency
            "S23",  # model
            256,  # memory
            "Gray"  # color
        )

        captured = capsys.readouterr()

        assert captured.out != ""
        assert "Smartphone(" in captured.out
