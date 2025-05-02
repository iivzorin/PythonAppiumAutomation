from main import MainClass

class TestMainClass:
    def test_get_local_number(self):
        obj = MainClass()
        result = obj.get_local_number()
        assert result == 14, "Ошибка: метод get_local_number должен возвращать число 14"
