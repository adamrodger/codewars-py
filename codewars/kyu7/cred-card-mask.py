# https://www.codewars.com/kata/5412509bd436bd33920011bc/solutions/python
def maskify(cc):
    return ("#" * (len(cc) - 4)) + cc[-4:]