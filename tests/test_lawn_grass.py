from src.lawn_grass import LawnGrass


class TestLawnGrass:
    def test_initialization(self):
        g = LawnGrass(
            "Grass", "For lawn", 200.0, 10,
            country="Russia", germination_period="7 days", color="Green"
        )
        assert g.name == "Grass"
        assert g.country == "Russia"

    def test_add_operation(self):
        g1 = LawnGrass("G1", "D1", 100.0, 5, "RU", "5d", "G")
        g2 = LawnGrass("G2", "D2", 100.0, 5, "BY", "6d", "DG")
        result = g1 + g2
        assert isinstance(result, LawnGrass)
        assert result.price == 200.0
        assert result.quantity == 10

    def test_describe(self):
        g = LawnGrass("Test", "Desc", 100.0, 1, "KZ", "10d", "LG")
        desc = g.describe()
        assert "Test" in desc
        assert "страна: KZ" in desc
