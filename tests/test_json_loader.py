import json
import pytest
from src.json_loader import load_categories_from_json
from src.models import Category


@pytest.fixture
def sample_json_path(tmp_path):
    data = [
        {
            "name": "Смартфоны",
            "description": "Мобильные устройства",
            "products": [
                {"name": "Samsung Galaxy S23 Ultra", "description": "256GB", "price": 180000.0, "quantity": 5},
                {"name": "Iphone 15", "description": "512GB", "price": 210000.0, "quantity": 8}
            ]
        },
        {
            "name": "Телевизоры",
            "description": "Домашний просмотр",
            "products": [
                {"name": "55\" QLED 4K", "description": "Подсветка", "price": 123000.0, "quantity": 7}
            ]
        }
    ]
    path = tmp_path / "products.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def test_load_categories_from_json_success(sample_json_path):
    categories = load_categories_from_json(str(sample_json_path))

    assert len(categories) == 2
    first = categories[0]
    assert isinstance(first, Category)
    assert first.name == "Смартфоны"
    assert len(first.products) == 2


def test_load_categories_from_json_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_categories_from_json("несуществующий_файл.json")


def test_load_categories_from_json_empty_file(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("[]", encoding="utf-8")

    categories = load_categories_from_json(str(path))
    assert len(categories) == 0


def test_load_categories_from_json_completely_invalid_json(tmp_path):
    # Это вообще не JSON — должен быть JSONDecodeError
    path = tmp_path / "broken.json"
    path.write_text("это вообще не json", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_categories_from_json(str(path))


def test_load_categories_from_json_invalid_structure(tmp_path):
    # Это валидный JSON, но не список (а словарь) — должен быть ValueError
    path = tmp_path / "wrong_structure.json"
    path.write_text('{"name": "Не список"}', encoding="utf-8")

    with pytest.raises(ValueError):
        load_categories_from_json(str(path))


def test_load_categories_from_json_category_without_products(tmp_path):
    data = [
        {
            "name": "Пустая категория",
            "description": "Нет товаров",
            "products": []
        }
    ]
    path = tmp_path / "no_products.json"
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    categories = load_categories_from_json(str(path))

    assert len(categories) == 1
    assert categories[0].name == "Пустая категория"
    assert len(categories[0].products) == 0
    assert categories[0].get_total_price() == 0.0


def test_load_categories_from_json_skips_malformed_entries(tmp_path):
    data = [
        {"name": "Нормальная категория", "products": [
            {"name": "Товар", "price": 100, "quantity": 1}
        ]},
        {"products": []},  # нет name → будет пропущен
        "это не словарь",  # вообще не dict → будет пропущен
        {
            "name": "Ещё одна",
            "products": [
                {"price": 100, "quantity": 1},  # нет name у товара → будет пропущен
                {"name": "Хороший товар", "price": "не число", "quantity": 1},  # price не число → будет пропущен
            ]
        }
    ]
    path = tmp_path / "malformed.json"
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    categories = load_categories_from_json(str(path))

    assert len(categories) == 2
    assert categories[0].name == "Нормальная категория"
    assert len(categories[0].products) == 1
    assert categories[1].name == "Ещё одна"
    # У второй категории товаров не будет, потому что оба были битые
    assert len(categories[1].products) == 0
