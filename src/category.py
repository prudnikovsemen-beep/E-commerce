from typing import List, Optional
from .product import Product


class Category:
    # Класс-атрибут: общий счётчик всех добавленных товаров
    product_count_total: int = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []
        if products:
            for p in products:
                # При инициализации тоже считаем добавления
                self.add_product(p)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        # Вот эта строка была пропущена — увеличиваем общий счётчик
        Category.product_count_total += 1

    @property
    def products(self) -> str:
        lines: List[str] = []
        for p in self.__products:
            lines.append(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.")
        return "\n".join(lines)

    @property
    def product_count(self) -> int:
        """Количество товаров именно в этой категории."""
        return len(self.__products)

    @classmethod
    def get_total_product_count(cls) -> int:
        """Возвращает общее количество добавленных товаров (по всем категориям)."""
        return cls.product_count_total

    def get_products_list(self) -> List[Product]:
        """Вспомогательный метод для вывода (не нарушает инкапсуляцию)."""
        return self.__products.copy()
