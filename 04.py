"""Never Gonna Give You Up"""


def main():
    """Never Gonna Give You Up"""
    for i in input():
        if not i.isalnum():
            print(i, end="")
            continue
        var_a = 97
        if i.isupper():
            var_a = 65
        shifting = 26 - (ord(i) - var_a)
        print(chr(shifting + (var_a - 1)), end="")


main()
