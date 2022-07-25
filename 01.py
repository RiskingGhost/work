"""This programme do somthing"""


def main():
    """Main function"""
    grade = float(input())
    if grade >= 2.00:
        print("I'm so happy.")
    elif grade < 1.00:
        print("I'm so sad.")
    else:
        print("{:.2f}".format(4.00 - grade))


if __name__ == "__main__":
    main()
