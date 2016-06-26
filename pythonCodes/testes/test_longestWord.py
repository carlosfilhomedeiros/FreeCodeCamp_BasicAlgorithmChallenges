from context import sample
from sample import longestWord
import unittest


class KnwonValues(unittest.TestCase):
    casos = (("Hoje Estarei Livre", 7),
             ("Ontem Sim", 5))

    def test_answer(self):
        '''longestWord should return the kwon values with known inputs '''
        for frase, tam in self.casos:
            resultado = longestWord.longestWord(frase)
            self.assertEqual(resultado, tam)

if __name__ == '__main__':
    unittest.main()
