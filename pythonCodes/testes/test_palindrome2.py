from context import sample
from sample import palindrome
import unittest


class MyTest(unittest.TestCase):
    casos = (("casa", False),
             ("asa", True),
             ("ola", False))

    def test_answer(self):
        '''Palindrome should return True is a Word is one,Else False '''
        for palavra, TrueOrFalse in self.casos:
            resultado = palindrome.palindrome(palavra)
            self.assertEqual(TrueOrFalse, resultado)

if __name__ == '__main__':
    unittest.main()
