# https://www.codewars.com/kata/decode-the-morse-code-advanced/train/python

def decodeBits(bits):
    bits = bits.strip('0') # remove extra 0s
    
    if '0' not in bits:
        return '.' # entire message is all 1s, so it's a dot
    
    import re
    ones = sorted(len(x) for x in re.findall("1+", bits))
    zeroes = sorted(len(x) for x in re.findall("0+", bits))
    time_unit = min(ones[0], zeroes[0])
    
    result = bits.replace('0000000' * time_unit, '   ') \
                 .replace('111' * time_unit, '-') \
                 .replace('000' * time_unit, ' ') \
                 .replace('1' * time_unit, '.') \
                 .replace('0' * time_unit, '')
    return result

def decodeMorse(morseCode):
    words = morseCode.strip().split('   ')
    return " ".join(["".join([MORSE_CODE[letter] for letter in word.split()]) for word in words])

MORSE_CODE={'.-...': '&',
            '--..--': ',',
            '....-': '4',
            '.....': '5',
            '...---...': 'SOS',
            '-...': 'B',
            '-..-': 'X',
            '.-.': 'R',
            '.--': 'W',
            '..---': '2',
            '.-': 'A',
            '..': 'I',
            '..-.': 'F',
            '.': 'E',
            '.-..': 'L',
            '...': 'S',
            '..-': 'U',
            '..--..': '?',
            '.----': '1',
            '-.-': 'K',
            '-..': 'D',
            '-....': '6',
            '-...-': '=',
            '---': 'O',
            '.--.': 'P',
            '.-.-.-': '.',
            '--': 'M',
            '-.': 'N',
            '....': 'H',
            '.----.': "'",
            '...-': 'V',
            '--...': '7',
            '-.-.-.': ';',
            '-....-': '-',
            '..--.-': '_',
            '-.--.-': ')',
            '-.-.--': '!',
            '--.': 'G',
            '--.-': 'Q',
            '--..': 'Z',
            '-..-.': '/',
            '.-.-.': '+',
            '-.-.': 'C',
            '---...': ':',
            '-.--': 'Y',
            '-': 'T',
            '.--.-.': '@',
            '...-..-': '$',
            '.---': 'J',
            '-----': '0',
            '----.': '9',
            '.-..-.': '"',
            '-.--.': '(',
            '---..': '8',
            '...--': '3'}