from typing import List, Optional
from .product import Product


class Category:
    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = []
        if products:
            for p in products:
                self.add_product(p)

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    @property
    def products(self) -> str:
        lines: List[str] = []
        for p in self.__products:
            lines.append(f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.")
        return "\n".join(lines)

    @property
    def product_count(self) -> int:
        return len(self.__products)

    def get_products_list(self) -> List[Product]:
        """Возвращает копию списка товаров для внутренней логики."""
        return self.__products.copy()
