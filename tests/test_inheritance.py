import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category

def test_smartphone_is_product():
    s = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert isinstance(s, Product)
    assert s.name == "Samsung Galaxy S23 Ultra"
    assert s.efficiency == 95.5
    assert s.model == "S23 Ultra"
    assert s.memory == 256
    assert s.color == "Серый"

def test_lawn_grass_is_product():
    g = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert isinstance(g, Product)
    assert g.country == "Россия"
    assert g.germination_period == "7 дней"
    assert g.color == "Зеленый"

def test_add_same_type():
    s1 = Smartphone("S1", "desc", 1000, 1, 90, "M1", 256, "Black")
    s2 = Smartphone("S2", "desc", 2000, 2, 92, "M2", 512, "White")
    result = s1 + s2
    # Проверь, что результат имеет смысл: например, сумма цен, количеств и т.п.
    assert result.price == s1.price + s2.price
    assert result.quantity == s1.quantity + s2.quantity

def test_add_different_types_raises_type_error():
    s = Smartphone("S", "desc", 1000, 1, 90, "M", 256, "Black")
    g = LawnGrass("G", "desc", 500, 10, "RU", "7 дней", "Green")
    with pytest.raises(TypeError):
        _ = s + g

def test_category_add_valid_product():
    cat = Category("Смартфоны", "Phones", [])
    p = Product("Test", "Desc", 100, 5)
    cat.add_product(p)
    assert len(cat.products) == 1
    assert cat.products[0] is p

def test_category_add_invalid_object_raises_type_error():
    cat = Category("Смартфоны", "Phones", [])
    with pytest.raises(TypeError):
        cat.add_product("Not a product")
