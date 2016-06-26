
def longestWord(str):
    ''' look into a string and find out what is the length of the longest word'''
    separado = str.split(" ")
    separado.sort(key=len)
    return len(separado[-1])
