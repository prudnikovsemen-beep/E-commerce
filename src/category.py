from .product import Product


class Category:
    product_count = 0  # глобальный счётчик всех товаров

    def __init__(self, name: str, slug: str, products=None):
        self.name = name
        self.slug = slug
        self._products = []

        # Добавляем товары через add_product, чтобы корректно увеличить product_count
        if products:
            for product in products:
                self.add_product(product)

    @classmethod
    def get_total_product_count(cls) -> int:
        return cls.product_count

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавить только объект Product")
        self._products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [str(p) for p in self._products]

    @property
    def product_count(self) -> int:
        # количество товаров именно в этой категории
        return len(self._products)

    def total_price(self) -> float:
        return sum(p.price for p in self._products)

    # --- Магические методы (только по одному экземпляру!) ---

    def __str__(self) -> str:
        total_qty = sum(p.quantity for p in self._products)
        return f"{self.name}, количество продуктов: {total_qty} шт."

    def __len__(self) -> int:
        return len(self._products)

    def __contains__(self, item: Product) -> bool:
        return item in self._products

    def __iter__(self):
        return iter(self._products)
