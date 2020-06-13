import math
import argparse
import sys


def check_parameters():
    if args.type != "annuity" and args.type != "diff" or \
            not args.type or not args.interest or \
            args.type == "diff" and args.payment or len(arg_list) != 5 or \
            args.principal is not None and args.principal < 0 or \
            args.periods is not None and args.periods < 0 or \
            args.interest < 0 or \
            args.payment is not None and args.payment < 0:
        print("Incorrect parameters")
        return False
    return True


def calculate_periods():
    periods = math.ceil(math.log(args.payment / (args.payment - args.interest
                                                 / 1200 * args.principal),
                                 1 + args.interest / 1200))
    years = periods // 12
    months = periods % 12
    plural_y = "s" if years > 1 else ""
    plural_m = "s" if months > 1 else ""
    if years == 0:
        print(f"You need {months} month{plural_m} to repay this credit!")
    elif months == 0:
        print(f"You need {years} year{plural_y} to repay this credit!")
    else:
        print(
            f"You need {years} year{plural_y} and {months} month{plural_y} to repay this credit!")
    overpayment = periods * args.payment - args.principal
    print(f"Overpayment = {overpayment}")


def calculate_payments():
    if args.type == "annuity":
        annuity_payment = math.ceil(
                args.principal * (args.interest/1200 *
                (1 + args.interest/1200)**args.periods) /
                ((1 + args.interest/1200)**args.periods - 1))
        print(f"Your annuity payment = {annuity_payment}!")
        overpayment = annuity_payment * args.periods - args.principal
    else:
        overpayment = -args.principal
        for i in range(1, args.periods + 1):
            monthly_payment = math.ceil(
                args.principal / args.periods + args.interest / 1200 * \
                (args.principal - (
                            args.principal * (i - 1) / args.periods)))
            print(f"Month {i}: paid out {monthly_payment}")
            overpayment += monthly_payment
        print()
    print(f"Overpayment = {overpayment}")


def calculate_principal():
    principal = int(args.payment / ((args.interest / 1200 * (
                (1 + args.interest / 1200) ** args.periods)) /
                (((1 + args.interest / 1200) ** args.periods) - 1)))
    print(f"Your credit principal = {principal}!")
    overpayment = args.periods * args.payment - principal
    print(f"Overpayment = {overpayment}")


def calculate():
    if not args.periods:
        calculate_periods()
    elif not args.payment:
        calculate_payments()
    elif not args.principal:
        calculate_principal()


if __name__ == "__main__":
    arg_list = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("--payment", type=int)
    args = parser.parse_args()
    if check_parameters():
        calculate()