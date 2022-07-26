"""This programme accumulate numbers"""


def main():
    """This is the main function"""

    int_accumulate = 0  # liar
    glb_num_not_found = False
    int_length = int(input())

    if int_length <= 0:
        print("No Tape Measure")
    else:
        while True:
            int_input = input()
            if int_input == "No more!":
                break
            elif int(int_input) > int_length:
                glb_num_not_found = True
                int_input = 0
            int_accumulate += int(int_input)

        if glb_num_not_found and int_accumulate == 0:
            print("Not Found Number")
        else:
            print("Sum of Found Number = {}".format(int_accumulate))


if __name__ == "__main__":
    main()
