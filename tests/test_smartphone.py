from src.smartphone import Smartphone


class TestSmartphone:
    def test_initialization(self):
        s = Smartphone(
            "iPhone", "Latest model", 1000.0, 5,
            efficiency=0.9, model="15 Pro", memory=256, color="Black"
        )
        assert s.name == "iPhone"
        assert s.model == "15 Pro"
        assert s.memory == 256

    def test_add_operation(self):
        s1 = Smartphone("S1", "Desc1", 500.0, 2, 0.8, "M1", 128, "Red")
        s2 = Smartphone("S2", "Desc2", 500.0, 2, 0.8, "M2", 128, "Blue")
        result = s1 + s2
        assert isinstance(result, Smartphone)
        assert result.price == 1000.0
        assert result.quantity == 4

    def test_describe(self):
        s = Smartphone("Test", "Desc", 100.0, 1, 0.5, "T1", 64, "Green")
        desc = s.describe()
        assert "Test" in desc
        assert "модель: T1" in desc
