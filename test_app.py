import unittest
from app import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Перевірка: додавання двох позитивних чисел."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 15), 25)

    def test_add_zero(self):
        """Перевірка: додавання з нулем."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 7), 7)
        self.assertEqual(add(5, 0), 5)

    def test_add_negative_numbers(self):
        """Перевірка: додавання від’ємних чисел."""
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(3, -5), -2)

    def test_add_large_numbers(self):
        """Перевірка: додавання дуже великих чисел."""
        large1 = 10**9
        large2 = 10**9
        self.assertEqual(add(large1, large2), 2 * 10**9)

    def test_add_floats(self):
        """Перевірка: додавання чисел з плаваючою крапкою."""
        self.assertAlmostEqual(add(2.5, 3.1), 5.6)
        self.assertAlmostEqual(add(-1.2, 1.2), 0.0)

    def test_add_mixed_types(self):
        """
        Перевірка: додавання цілих і дробових чисел.
        (У нашій функції add не реалізовано перевірку типів,
        тому такі випадки можуть викликати помилку.)
        """
        self.assertAlmostEqual(add(5, 2.5), 7.5)
        self.assertAlmostEqual(add(-3, 1.5), -1.5)

    def test_add_invalid_types(self):
        """
        Перевірка: спроба додати нечислові типи має викликати TypeError.
        """
        with self.assertRaises(TypeError):
            add("2", 3)
        with self.assertRaises(TypeError):
            add(None, 5)
        with self.assertRaises(TypeError):
            add([1, 2], 3)

if __name__ == '__main__':
    unittest.main()
