import unittest
from servidor.utils import verificar_maioridade

class TestServidor(unittest.TestCase):
    
    def test_verificar_maioridade(self):
        self.assertEqual(verificar_maioridade("João", "M", "20"), "João já atingiu a maioridade.")
        self.assertEqual(verificar_maioridade("Maria", "F", "19"), "Maria ainda não atingiu a maioridade.")
        self.assertEqual(verificar_maioridade("Carlos", "M", "17"), "Carlos ainda não atingiu a maioridade.")
        self.assertEqual(verificar_maioridade("Ana", "F", "21"), "Ana já atingiu a maioridade.")
    
    def test_verificar_maioridade_sexo_invalido(self):
        self.assertEqual(verificar_maioridade("Alex", "X", "25"), "Sexo inválido para Alex")

if __name__ == '__main__':
    unittest.main()
