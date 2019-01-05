# https://www.codewars.com/kata/the-observed-pin

def get_pins(input):
    import itertools 

    available = {
        "0": "08",
        "1": "124",
        "2": "1235",
        "3": "236",
        "4": "1457",
        "5": "24568",
        "6": "3569",
        "7": "478",
        "8": "57890",
        "9": "689"
    }

    digits = [c for c in input]
    possible_digits = [available[x] for x in digits]
    return ["".join(x) for x in itertools.product(*possible_digits)]
