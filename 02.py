"""This programme calculates snacks"""


def main():
    """This is the Entry point"""
    fl_money = float(input())
    int_water = int(input())
    int_snack_1 = int(input())
    int_snack_2 = int(input())
    int_snack_3 = int(input())

    money_minus_water = fl_money-int_water
    try:
        # snack mechine numero uno
        snack_1_out = snack_fac(money_minus_water, int_snack_1, 10, 15, 20)
    except:
        print("You don't have enough money!")


def snack_fac(arg_money: float, arg_amount: int,
              arg_price_1: int,
              arg_price_2: int,
              arg_price_3: int) -> float:
    """This is the snack factory, this returns net price of snacks \
        and if the money is not enough to buy snack it will throw exeption"""
    if arg_money % 3 == 0:
        snack_price = arg_amount*arg_price_1
    elif arg_money % 3 == 1:
        snack_price = arg_amount*arg_price_2
    elif arg_money % 3 == 2:
        snack_price = arg_amount*arg_price_3


if __name__ == "__main__":
    main()
