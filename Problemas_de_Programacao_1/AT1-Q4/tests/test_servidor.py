import unittest
from servidor.utils import calcular_peso_ideal

class TestServidor(unittest.TestCase):

    def test_calcular_peso_ideal(self):
        self.assertEqual(calcular_peso_ideal(1.75, 'M'), (72.7 * 1.75) - 58)
        self.assertEqual(calcular_peso_ideal(1.65, 'F'), (62.1 * 1.65) - 44.7)
        self.assertIsNone(calcular_peso_ideal(1.75, 'X'))

if __name__ == "__main__":
    unittest.main()
