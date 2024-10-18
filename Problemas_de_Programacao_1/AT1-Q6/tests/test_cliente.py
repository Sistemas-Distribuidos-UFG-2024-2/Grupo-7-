import unittest
from cliente.utils import validar_entrada

class TestCliente(unittest.TestCase):

    def test_validar_entrada(self):
        self.assertTrue(validar_entrada('1.75', 'M'))
        self.assertTrue(validar_entrada('1.65', 'F'))
        self.assertFalse(validar_entrada('abc', 'M'))
        self.assertFalse(validar_entrada('1.75', 'X'))

if __name__ == "__main__":
    unittest.main()
