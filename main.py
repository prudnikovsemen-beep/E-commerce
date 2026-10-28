from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawn_grass import LawnGrass

if __name__ == "__main__":
    print("=" * 60)
    print("ЧАСТЬ 1: Проверка исключений и валидации")
    print("=" * 60)

    # Проверка создания товара с quantity = 0 (должно выбросить ValueError)
    try:
        product_invalid = Product(
            "Бракованный товар",
            "Неверное количество",
            1000.0,
            0
        )
        print("❌ Ошибка НЕ возникла! Это плохо для теста.")
    except ValueError as e:
        print(f"✅ Возникла ошибка ValueError: {e}")

    # Проверка сеттера цены: отрицательная и нулевая цена
    test_prod = Product("Тест товар", "Описание", 100.0, 5)
    for bad_price in [-100, 0]:
        try:
            test_prod.price = bad_price
            print(f"❌ Сеттер НЕ отверг цену {bad_price}!")
        except ValueError:
            print(f"✅ Сеттер корректно отверг цену {bad_price}")

    print("\n" + "=" * 60)
    print("ЧАСТЬ 2: Базовые продукты и категории, счётчики")
    print("=" * 60)

    product1 = Product(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
    product2 = Product(
        "Iphone 15",
        "512GB, Gray space",
        210000.0,
        8
    )
    product3 = Product(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14
    )

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(f"Категория: {category1.name}")
    print(f"Описание: {category1.description}")
    # Используем property у экземпляра для количества товаров в этой категории
    print(f"Количество товаров в категории: {category1.product_count}")
    print(f"Всего категорий: {Category.category_count}")
    # Используем переменную класса для общего количества товаров во всех категориях
    print(f"Всего товаров (во всех категориях): {Category.total_product_count}")

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    print(f"\nКатегория: {category2.name}")
    print(f"Товары: {category2.products}")

    print(f"\nВсего категорий: {Category.category_count}, всего товаров: {Category.total_product_count}")

    print("\n" + "=" * 60)
    print("ЧАСТЬ 3: Метод middle_price и пустые категории")
    print("=" * 60)

    print(f"Средняя цена в категории 'Смартфоны': {category1.middle_price():.2f}")

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()}")  # Должно быть 0.0

    print("\n" + "=" * 60)
    print("ЧАСТЬ 4: Подклассы (Smartphone, LawnGrass), магические методы и add_product")
    print("=" * 60)

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5,
        95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8,
        98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14,
        90.3, "Note 11", 1024, "Синий"
    )

    grass1 = LawnGrass(
        "Газонная трава", "Элитная трава для газона", 500.0, 20,
        "Россия", "7 дней", "Зеленый"
    )
    grass2 = LawnGrass(
        "Газонная трава 2", "Выносливая трава", 450.0, 15,
        "США", "5 дней", "Темно-зеленый"
    )

    # Демонстрация атрибутов подклассов
    print(f"\nСмартфон: {smartphone1.name}, эффективность: {smartphone1.efficiency}, модель: {smartphone1.model}")
    print(f"Трава: {grass1.name}, страна: {grass1.country}, цвет: {grass1.color}")

    # Магические методы: сложение объектов
    smartphone_sum = smartphone1 + smartphone2
    print(f"Сумма двух смартфонов: {smartphone_sum}")

    grass_sum = grass1 + grass2
    print(f"Сумма двух видов травы: {grass_sum}")

    # Попытка сложить разные типы (должна вызвать TypeError)
    try:
        invalid_sum = smartphone1 + grass1
        print("❌ Не возникла ошибка TypeError при сложении разных типов!")
    except TypeError:
        print("✅ Возникла ожидаемая ошибка TypeError при попытке сложения разных типов.")

    # Работа с категорией и add_product
    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_smartphones.add_product(smartphone3)
    print(f"Товары в категории смартфонов после add_product: {category_smartphones.products}")

    # Защита от добавления не-продукта
    try:
        category_smartphones.add_product("Not a product")
        print("❌ add_product НЕ отверг не-продукт!")
    except TypeError:
        print("✅ add_product корректно отверг не-объект Product.")

    print(f"\nИтого товаров во всех категориях: {Category.total_product_count}")

    print("\n" + "=" * 60)
    print("ЧАСТЬ 5: Factory-метод new_product и строковое представление")
    print("=" * 60)

    new_product = Product.new_product({
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    })
    print(f"Продукт через new_product: {new_product}")

    # Демонстрация __str__
    print(f"Строковое представление product1: {str(product1)}")
    print(f"Строковое представление category1: {str(category1)}")

    print("\n✅ Все демонстрации завершены.")
