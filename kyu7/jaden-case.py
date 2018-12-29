# https://www.codewars.com/kata/jaden-casing-strings/train/python

def toJadenCase(s):
    return " ".join([x.capitalize() for x in s.split()])