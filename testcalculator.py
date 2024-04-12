import unittest
from calculator import Calculator  # Suponiendo que tienes una clase Calculator en un módulo llamado calculator

class TestCalculator(unittest.TestCase):
    # Definimos el método setUp para inicializar una instancia de la calculadora antes de cada prueba
    def setUp(self):
        self.calculator = Calculator()

    # Prueba de suma
    def test_addition(self):
        result = self.calculator.add(2, 3)
        self.assertEqual(result, 5)

    # Prueba de resta
    def test_subtraction(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()