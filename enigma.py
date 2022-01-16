
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rotor(word: str, n: int, reverse=False) -> str:
    global ALPHABET
    rot = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
           2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE', 3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO'}
    return ALPHABET[rot[n].find(word) % len(ALPHABET)] if reverse else rot[n][ALPHABET.find(word) % len(rot[n])]


def reflector(word: str, n: int) -> str:
    global ALPHABET
    ref = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT'}
    return ref[n][ALPHABET.find(word) % len(ref[n])]


def changing(word: str, key: int) -> str:
    global ALPHABET
    return ALPHABET[(ALPHABET.find(word) + key) % len(ALPHABET)]


def switching(word: str, pairs: list) -> str:
    for i in pairs:
        if word in i:
            return i[(i.find(word) + 1) % 2]
    return word


def enigma(text: str, ref: int, rot1: int, shift1: int, rot2: int,
           shift2: int, rot3: int, shift3: int, pairs="") -> str:
    if pairs:
        check = [i.upper() for i in pairs.split() if i.isalpha()]

        if len(set(''.join(check))) != len(''.join(check)):
            return 'Извините, невозможно произвести коммутацию'
        switch = check
    else:
        switch = []
    t = ''.join(text.upper().split())
    original = {1: 17, 2: 5, 3: 22}
    x = [rot3, rot2, rot1]
    y = [shift3, shift2, shift1]
    s = ''

    for word in t:

        y[0] = (y[0] + 1) % 26
        if y[0] == original[rot3]:
            y[1] = (y[1] + 1) % 26

        word = switching(word, switch)

        for j in range(3):
            word = changing(rotor(changing(word, y[j]), x[j]), y[j] * (-1))

        word = reflector(word, ref)

        for k in range(2, -1, -1):
            word = changing(rotor(changing(word, y[k]), x[k], reverse=True), y[k] * (-1))

        word = switching(word, switch)

        s += word

        if (y[1] + 1) == original[rot2]:
            y[1] = (y[1] + 1) % 26
            y[2] = (y[2] + 1) % 26

    return s


def main():
    text = input("Enter your text to encrypt / decrypt (only english words):")
    t = ''.join([i for i in text.upper() if i in ALPHABET])
    while not len(t):
        text = input("Please enter your text to encrypt or decrypt again (only english words):")
        t = ''.join([i for i in text.upper() if i in ALPHABET])
    question = input('Now enter "1" if you need to make "Enigma" settings either enter "0" or leave the field empty:')
    if question or not question == 0:
        print('Your encrypted / decrypted text:', enigma(t, 1, 1, 0, 2, 0, 3, 0, ''))
    else:
        while question and question != 1:
            question = input('Please enter "1" again if you need to make "Enigma"'
                             ' settings either enter "0" or leave the field empty:')

        params = input('Enter the space-separated parameters for rotor1, rotor 2, rotor3 '
                       '(from 0 to 3 inclusive), for the displacement of the rotors from '
                       'the initial position (for each rotor), the reflector number (0 or 1)'
                       ' and the switching parameters (optional) in this order: ')
        flag = False
        if len(params.split()) != 7 or len(params.split()) != 8:
            flag = True

        else:
            s = params.split()
            r1, r2, r3, sh1, sh2, sh3, rf = map(int, s[:7])
            if len(params.split()) == 7:
                pa = ''
            else:
                pa = s[-1]

            print('Your encrypted / decrypted text:', enigma(t, rf, r1, sh1, r2, sh2, r3, sh3, pa))


if __name__ == "__main__":
    main()

