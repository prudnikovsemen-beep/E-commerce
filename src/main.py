from src.models import Product, Category
from src.json_loader import load_categories_from_json


def print_product(p: Product, indent: str = "") -> None:
    print(f"{indent}📦 {p.name}")
    print(f"{indent}   Цена: {p.price:,.0f} ₽, шт: {p.quantity}")
    print(f"{indent}   Описание: {p.description}")


def print_category(cat: Category, idx: int) -> None:
    print(f"\n=== Категория #{idx}: {cat.name} ===")
    print(f"Описание: {cat.description}")
    print(f"Товаров в категории: {len(cat.products)}")

    for p in cat.products:
        print_product(p, indent="   ")

    total = cat.get_total_price()
    print(f"Общая стоимость товаров в категории: {total:,.0f} ₽")


if __name__ == "__main__":
    print("--- Часть 1: Ручное создание объектов (как в задании) ---")
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод по каждому товару (понятно, а не просто значение)
    for i, p in enumerate([product1, product2, product3], start=1):
        print(f"\nТовар {i}:")
        print_product(p)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print_category(category1, idx=1)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    print_category(category2, idx=2)

    print("\n--- Глобальные счётчики (после ручного создания) ---")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")

    print("\n\n--- Часть 2: Загрузка из JSON (data/products.json) ---")
    try:
        loaded_categories = load_categories_from_json("data/products.json")

        for i, cat in enumerate(loaded_categories, start=1):
            print_category(cat, idx=i)

        print("\n--- Глобальные счётчики (после загрузки из JSON) ---")
        print(f"Всего категорий: {Category.category_count}")
        print(f"Всего товаров: {Category.product_count}")

    except FileNotFoundError as e:
        print(f"⚠️ Файл data/products.json не найден: {e}")
        print("Создай папку data и положи туда products.json с данными.")