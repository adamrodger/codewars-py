from codewars.kyu2.morse_code_3 import decodeBitsAdvanced, decodeMorse

def test_hey_jude():
    encoded = decodeBitsAdvanced("0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000")
    assert encoded == ".... . -.--   .--- ..- -.. ."

    decoded = decodeMorse(encoded)
    assert decoded == "HEY JUDE"