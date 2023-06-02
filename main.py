def AddC(a, b, c, d):
    for elem in (a, b, c, d):
        if not type(elem) in (int, float):
            return "Wrong argument type"
    re = a + c
    im = b + d
    return re, im


def SubC(a, b, c, d):
    for elem in (a, b, c, d):
        if not type(elem) in (int, float):
            return "Wrong argument type"
    re = a - c
    im = b - d
    return re, im


def MulC(a, b, c, d):
    for elem in (a, b, c, d):
        if not type(elem) in (int, float):
            return "Wrong argument type"
    re = a*c - b*d
    im = a*d + b*c
    return re, im


def DivC(a, b, c, d):
    for elem in (a, b, c, d):
        if not type(elem) in (int, float):
            return "Wrong argument type"
    try:
        re = (a*c + b*d)/(c*c + d*d)
        im = (b*c - a*d)/(c*c + d*d)
    except ZeroDivisionError:
        return "Cannot divide by zero"
    else:
        return re, im


if __name__ == "__main__":
    print(AddC(3, 2.4, 2, 7))
    print(SubC(10, 2, -4, 8))
    print(MulC(0.25, 0, 4, 2))
    print(DivC(17, 31, 2, 1))

