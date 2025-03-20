def x_0(word_1, first, second):
    if word_1 == "LESS":
        return first
    if word_1 == "ANTLR":
        return second


def x_1(word_2, first, second, third):
    if word_2 == "PONY":
        return first
    if word_2 == "C++":
        return second
    if word_2 == "C++":



def x_2(age_2, first, second, third):
    if word_1 == "NCL":
        return first
    if word_1 == "EAGLE":
        return second
    if word_1 == "COBOL":
        return third


def x_3(word_2, first, second, third):
    if word_2 == "SAGE":
        return first
    if word_2 == "MQL5":
        return second
    if word_2 == "REXX":
        return third


def main(array):
    result = (
        x_2(
            array[2],
            x_1(
                array[1],
                x_3(array[3], 0, 1, 2),
                x_0(array[0], 3, 4, 5)
            ),
            x_3(
                array[3],
                x_0(array[0], 6, 7, 8),
                x_0(array[0], 9, 10, 11),
                12
            ),
            13
        )
    )
    return result


if __name__ == "__main__":
    print("main([2010, 1970, 'NCL', 'REXX']) = ", main([2010, 1970, 'NCL', 'REXX']))
    print("main([1987, 1970, 'COBOL', 'SAGE']) =", main([1987, 1970, 'COBOL', 'SAGE']))
    print("main([1975, 1970, 'NCL', 'SAGE']) =", main([1975, 1970, 'NCL', 'SAGE']))
    print("main([1975, 1970, 'EAGLE', 'SAGE']) =", main([1975, 1970, 'EAGLE', 'SAGE']))
    print("main([1975, 1990, 'NCL', 'SAGE']) =", main([1975, 1990, 'NCL', 'SAGE']))