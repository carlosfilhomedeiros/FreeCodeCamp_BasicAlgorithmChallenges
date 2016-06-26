from context import sample
from sample import caseSentence
import unittest


class KnownValues(unittest.TestCase):
    casos = (("hoje eu preciso", "Hoje Eu Preciso"),
             ("eu e voce", "Eu E Voce"))

    def testAnswer(self):
        for frase, capitalizado in self.casos:
            resultado = caseSentence.caseSentence(frase)
            self.assertEqual(capitalizado, resultado)

if __name__ == '__main__':
    unittest.main()
