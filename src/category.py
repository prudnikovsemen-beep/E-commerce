from typing import List, Optional, Iterator
from .product import Product


class Category:
    # Глобальный счётчик всех товаров во всех категориях
    total_products_count: int = 0

    def __init__(self, name: str, slug: str, products: Optional[List[Product]] = None) -> None:
        self.name: str = name
        self.slug: str = slug
        self._products: List[Product] = []

        if products:
            for product in products:
                self.add_product(product)

    @classmethod
    def get_total_product_count(cls) -> int:
        return cls.total_products_count

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект Product")
        self._products.append(product)
        Category.total_products_count += 1

    @property
    def products(self) -> List[str]:
        return [str(p) for p in self._products]

    # Количество товаров именно в этой категории
    @property
    def product_count(self) -> int:
        return len(self._products)

    def total_price(self) -> float:
        return sum(p.price for p in self._products)

    # --- Магические методы ---

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __len__(self) -> int:
        return len(self._products)

    def __contains__(self, item: Product) -> bool:
        return item in self._products

    # Вот тут была ошибка: не хватало аннотации возврата
    def __iter__(self) -> Iterator[Product]:
        return iter(self._products)
