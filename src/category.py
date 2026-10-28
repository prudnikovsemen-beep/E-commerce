from typing import List, Optional, Iterator
from .product import Product


class Category:
    # Глобальные счётчики
    category_count: int = 0
    total_product_count: int = 0  # общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name: str = name
        self.description: str = description
        self._products: List[Product] = []

        Category.category_count += 1

        if products:
            for product in products:
                self.add_product(product)

    @classmethod
    def get_total_product_count(cls) -> int:
        return cls.total_product_count

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект Product")
        self._products.append(product)
        Category.total_product_count += 1

    @property
    def products(self) -> List[Product]:
        return self._products

    @property
    def product_count(self) -> int:
        """Количество товаров именно в этой категории"""
        return len(self._products)

    def total_price(self) -> float:
        return sum(p.price for p in self._products)

    def middle_price(self) -> float:
        """Средняя цена товаров в категории. Если товаров нет — возвращает 0.0"""
        if len(self._products) == 0:
            return 0.0
        total = sum(p.price for p in self._products)
        return total / len(self._products)

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __len__(self) -> int:
        return len(self._products)

    def __contains__(self, item: Product) -> bool:
        return item in self._products

    def __iter__(self) -> Iterator[Product]:
        return iter(self._products)
