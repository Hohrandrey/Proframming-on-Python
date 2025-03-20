"""
#1
def x_0(word_1, first, second):
    if word_1 == "LESS":
        return first
    if word_1 == "ANTLR":
        return second


def x_1(age_1, first, second):
    if age_1 == 1965:
        return first
    if age_1 == 1958:
        return second


def x_2(age_2, first, second, third):
    if age_2 == 1990:
        return first
    if age_2 == 2018:
        return second
    if age_2 == 2005:
        return third


def x_3(word_2, first, second, third):
    if word_2 == "PONY":
        return first
    if word_2 == "C++":
        return second
    if word_2 == "MIRAH":
        return third


def main(array):
    result = x_1(
        array[1],
        x_2(
            array[2],
            x_0(array[0], 0, 1),
            x_3(array[3], 2, 3, 4),
            x_3(array[3], 5, 6, 7)
        ),
        x_2(array[2], 8, 9, 10)
    )
    return result

"""

#2
tuple = (
    {1965, 1990, 'LESS'},
    {1965, 1990, 'ANTLR'},
    {1965, 2018, 'PONY'},
    {1965, 2018, 'C++'},
    {1965, 2018, 'MIRAH'},
    {1965, 2005, 'PONY'},
    {1965, 2005, 'C++'},
    {1965, 2005, 'MIRAH'},
    {1958, 1990},
    {1958, 2018},
    {1958, 2005}
)


def main(r):
    s = set(r)
    return [i for i in range(len(tuple)) if not (len(tuple[i] - s))][0]

if __name__ == "__main__":
    print(
        "main(['LESS', 1965, 2018, 'MIRAH']) = ",
        main(['LESS', 1965, 2018, 'MIRAH'])
    )
    print(
        "main(['LESS', 1958, 2005, 'PONY']) =",
        main(['LESS', 1958, 2005, 'PONY'])
    )
    print(
        "main(['LESS', 1965, 2005, 'C++']) =",
        main(['LESS', 1965, 2005, 'C++'])
    )
    print(
        "main(['ANTLR', 1965, 2018, 'C++']) =",
        main(['ANTLR', 1965, 2018, 'C++'])
    )
    print(
        "main(['ANTLR', 1958, 2018, 'C++']) =",
        main(['ANTLR', 1958, 2018, 'C++'])
    )
