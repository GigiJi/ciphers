# ----------------------Index Sub Cipher----------------------
def encryptIndexSubstitutionCipher(text):
    final = ''
    for i in text:
        if ord(i) - ord('a') < 9:
            final += '0' + str(ord(i) - ord('a') + 1)
        else:
            final += str(ord(i) - ord('a') + 1)
        final += ' '
    return final.rstrip()
def decryptIndexSubstitutionCipher(text):
    final = ''
    for i in range(0, len(text), 3):
        x = int(text[i]) * 10
        x += int(text[i+1]) + ord('a') - 1
        final += chr(x)
    return final
# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}
def encryptMorseCode(text):
    for i in text:
        value = morseCode[i] + " "
        text = text.replace(i, value)
    return text.rstrip()
def decryptMorseCode(text):
    final, stri = '', ''
    arr = []
    for i in text:
        if i != ' ':
            stri += i
        else:
            arr.append(stri)
            stri = ''
    arr.append(stri)
    for char in arr:
        for i in morseCode:
            if char == morseCode[i]:
                final += i
    return final
# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    final = ''
    for i in text:
        index = (a * (ord(i) - ord('a')) + b) % 26
        index = chr(index + ord('a'))
        final += index
    return final
    # alphString = ''
    # for i in range(97,123):
    #     alphString+=chr(i)
    # alphabetArr = list(alphString)  # Array that contains lowercase alphabet letters
    # arr = []
    # for i in text:
    #     index = alphabetArr.index(i)
    #     index = (a * index + b) % 26
    #     arr.append(alphabetArr[index])
    # arr = ''.join(str(i) for i in arr)
    # return arr

def decryptAffineCipher(text, a, b):
    alphString = ''
    for i in range(97,123):
        alphString+=chr(i)
    alphabetArr = list(alphString)  # Array that contains lowercase alphabet letters
    arr = []
    for i in text:
        index = alphabetArr.index(i)
        index = (pow(a, -1, 26) * (index - b)) % 26
        arr.append(alphabetArr[index])
    arr = ''.join(str(i) for i in arr)
    return arr
# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    lalphString =''
    for i in range(97,123):
        lalphString+=chr(i)
    ualphString = lalphString.upper()
    lower = list(lalphString)
    upper = list(ualphString)
    numArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    arr = []
    for i in text:
        arr.append(i)
    for i in range(len(arr)):
        if i % 2 == 0:
            key = key1
        else:
            key = key2
        if arr[i].isalpha():
            if arr[i].islower():
                array = lower
            else:
                array = upper
            newchar = array[(array.index(arr[i]) + key) % len(array)]
        else:
            if arr[i].isnumeric():
                newchar = numArr[(numArr.index(arr[i]) + key) % len(numArr)]
            else:
                newchar = arr[i]
        arr.pop(i)
        arr.insert(i, newchar)
        result = ''.join(str(i) for i in arr)
    return result
def decryptCaesarCipher(text, key1, key2):
    lalphString = ''
    for i in range(97, 123):
        lalphString += chr(i)
    ualphString = lalphString.upper()
    lower = list(lalphString)
    upper = list(ualphString)
    numArr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    arr = []
    for i in text:  # Moving all of the characters of the text into an array 'arr'
        arr.append(i)
    for i in range(len(arr)):
        if i % 2 == 0:
            key = key1
        else:
            key = key2
        if arr[i].isalpha():
            if arr[i].islower():
                array = lower
            else:
                array = upper
            newchar = array[(array.index(arr[i]) - key) % len(array)]
        else:
            if arr[i].isnumeric():
                newchar = numArr[(numArr.index(arr[i]) - key) % len(numArr)]
            else:
                newchar = arr[i]
        arr.pop(i)
        arr.insert(i, newchar)
        result = ''.join(str(i) for i in arr)
    return result
# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    arr, str = list(text), ''
    for i in range(key):
        for index in range(i,len(arr), key):
            str += arr[index]
    return str
def decryptTranspositionCipher(text, key):
    quotient = int(len(text)/key)
    remainder = len(text) % key
    str = ''
    if remainder != 0:
        for i in range(quotient + 1):
            x = remainder
            index = i
            while index < len(text):
                str += text[index]
                index += quotient
                if x > 0:
                    x -= 1
                    index += 1
                if x == 0 and i == quotient:
                    break
    else:
        for i in range(quotient ):
            index = i
            while index < len(text):
                str += text[index]
                index += quotient
    return str