from typing import List, Optional

from .product import Product


class Category:
    _total_product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        self.name = name
        self.description = description
        # Инициализируем список товаров, но НЕ трогаем счётчик!
        self.__products: List[Product] = list(products) if products else []
        # ❌ НИКАКИХ строк вида Category._total_product_count += ... ЗДЕСЬ БЫТЬ НЕ ДОЛЖНО!

    @property
    def products(self) -> List[str]:
        # Возвращаем строки для совместимости со старыми тестами
        return [str(p) for p in self.__products]

    def get_products_objects(self) -> List[Product]:
        # Возвращаем объекты для main.py
        return list(self.__products)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        # ✅ Увеличиваем счётчик ТОЛЬКО здесь
        Category._total_product_count += 1

    @property
    def product_count(self) -> int:
        return len(self.__products)

    @classmethod
    def get_total_product_count(cls) -> int:
        return cls._total_product_count

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_qty} шт."
