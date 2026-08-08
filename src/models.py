class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    # Атрибуты класса (счётчики)
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.products = products

        # Увеличиваем счётчики
        Category.category_count += 1
        Category.product_count += len(products)

    def get_total_price(self) -> float:
        """
        Возвращает общую стоимость всех товаров в категории.
        Формула: сумма (цена * количество) по всем товарам.
        """
        return sum(p.price * p.quantity for p in self.products)
