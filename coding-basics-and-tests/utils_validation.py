import unittest
import utils


class UtilTest(unittest.TestCase):

    def test_valida_maiuscula(self):
        resultado = utils.mudar_para_maiuscula("julio")
        self.assertEqual(resultado, "JULIO",
                         "Funcao deveria retornar JULIO em caps")

    def test_valida_minuscula(self):
        resultado = utils.mudar_para_minuscula("JULIO")
        self.assertEqual(resultado, "julio",
                         "Funcao deveria retornar julio")

    def test_valida_randonico(self):
        r = utils.gerar_numero_aleatorio()
        self.assertIn("X", r)

    def test_valida_idade(self):
        r = utils.calcular_idade(ano_nascimento=2000)
        self.assertEquals(20, r)


if __name__ == '__main__':
    unittest.main()
