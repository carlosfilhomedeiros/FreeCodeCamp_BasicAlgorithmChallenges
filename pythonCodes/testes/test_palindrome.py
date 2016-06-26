from context import sample
from sample import palindrome


def test_answer():
    assert palindrome.palindrome("casa") == False
    assert palindrome.palindrome("ovo") == True
