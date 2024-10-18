import unittest
from cliente.utils import formata_dados

class TestCliente(unittest.TestCase):
    
    def test_formata_dados(self):
        self.assertEqual(formata_dados("João", "M", "25"), "João,M,25")
        self.assertEqual(formata_dados("Maria", "F", "30"), "Maria,F,30")

if __name__ == '__main__':
    unittest.main()
