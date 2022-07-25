"""This programme does something"""

func_x = lambda arg: arg+1
func_y = lambda arg: arg**2

def main():
    """Entry point a.k.a. the main function"""
    str_input = str(input("Entre name: "))
    int_odds = list(map(lambda arg: (arg*2)-1, range(1,10)))
    print("Hello, \"{}\"!".format(str_input))
    for i in int_odds:
        print(func_x(func_y(i)))

if __name__ == "__main__":
    main()
