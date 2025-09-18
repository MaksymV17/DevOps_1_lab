import unittest
from feature.functions import check_string_case
from feature.generator import even_odd_generator

class TestFunctions(unittest.TestCase):
    def test_uppercase(self):
        self.assertEqual(check_string_case("HELLO"), "Усі літери великі")

    def test_lowercase(self):
        self.assertEqual(check_string_case("hello"), "Усі літери малі")

    def test_mixed(self):
        self.assertEqual(check_string_case("Hello"), "Змішаний регістр")

    def test_not_string(self):
        self.assertEqual(check_string_case(123), "Помилка: очікувався рядок")

class TestGenerator(unittest.TestCase):
    def test_even_odd(self):
        gen = even_odd_generator()
        self.assertEqual(next(gen), "Парне")
        self.assertEqual(next(gen), "Непарне")
        self.assertEqual(next(gen), "Парне")

if __name__ == "__main__":
    unittest.main()
