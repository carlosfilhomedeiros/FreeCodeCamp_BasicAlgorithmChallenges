
def palindrome(val):
    '''If the word is an Palindrome, returns True
    else returns False'''

    if (val == val[::-1]):
        return True
    else:
        return False
