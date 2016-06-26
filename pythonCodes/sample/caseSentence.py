
def caseSentence(str):
    def upFirstLetter(strin):
        return strin[0].upper() + strin[1::1]
    str = str.lower()
    str = str.split(" ")
    str = list(map(upFirstLetter, str))
    return " ".join(str)
