from main import MainClass

class TestMainClass:
    def test_get_local_number(self):
        main_class = MainClass()
        result = main_class.get_local_number()
        assert result == 14, "Ошибка: метод get_local_number должен возвращать число 14"

    def test_get_class_number(self):
        main_class = MainClass()
        result = main_class.get_class_number()

        assert result > 45, "Ошибка: метод get_class_number должен возвращать число больше 45"