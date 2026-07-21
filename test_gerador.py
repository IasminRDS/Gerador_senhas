"""Testes do gerador de senhas. Rode com: python -m unittest -v"""

import string
import unittest

from gerador import (
    CARACTERES_AMBIGUOS,
    calcular_entropia,
    classificar_forca,
    construir_alfabeto,
    gerar_senha,
)


class TestGerador(unittest.TestCase):
    def test_tamanho_correto(self):
        self.assertEqual(len(gerar_senha(20)), 20)

    def test_apenas_minusculas(self):
        senha = gerar_senha(50, maiusculas=False, numeros=False, simbolos=False)
        self.assertTrue(all(c in string.ascii_lowercase for c in senha))

    def test_sem_ambiguos(self):
        alfabeto = construir_alfabeto(sem_ambiguos=True)
        for c in CARACTERES_AMBIGUOS:
            self.assertNotIn(c, alfabeto)

    def test_numeros_incluidos_no_alfabeto(self):
        alfabeto = construir_alfabeto(numeros=True)
        self.assertTrue(any(c in string.digits for c in alfabeto))

    def test_entropia_cresce_com_tamanho(self):
        self.assertGreater(calcular_entropia(20, 90), calcular_entropia(8, 90))

    def test_classificacao_forca(self):
        self.assertIn("Fraca", classificar_forca(20))
        self.assertIn("Muito forte", classificar_forca(120))


if __name__ == "__main__":
    unittest.main()
