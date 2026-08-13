# E-commerce/main.py
from src.product import Product
from src.category import Category

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации...",
        [product1, product2, product3]
    )

    print(str(category1))

    # --- ДЛЯ СТАРЫХ ТЕСТОВ (совместимость) ---
    # Этот вывод теперь покажет список строк. Тесты будут довольны.
    print("Список товаров (строки для тестов):")
    print(category1.products)

    # --- ДЛЯ НОРМАЛЬНОЙ РАБОТЫ (твой код) ---
    # Используем НОВЫЙ метод, чтобы получить объекты и работать с ними
    print("\nСписок товаров (объекты для работы):")
    for p in category1.get_products_objects():
        print(f"Товар: {p.name}, Цена: {p.price}, Кол-во: {p.quantity}")

    print("\nРезультаты сложения (__add__):")
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
