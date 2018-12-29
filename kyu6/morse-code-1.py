# https://www.codewars.com/kata/decode-the-morse-code/train/python

def decodeMorse(morse_code):
    words = morse_code.strip().split('   ')
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