
import os


def print_menu():
    print("*" * 40)
    print("Warehouse management system")
    print("*" * 40)
    print("menu:")
    print(" [1] Register Product")
    print(" [2] Print catalog")
    print(" [3] Report: Products out of stock")
    print(" [4] Report: Stock Value")
    print(" [5] Report: Cheapest product")
    print(" [6] Delete product")
    print(" [7] Update  this product")  # ( price and stock )
    print(" [8] Report categories")

    print(" [x] Quit")


def clear_screen():
    if(os.name == "nt"):
        os.system("cls")
    else:
        os.system("clear")


def print_header(header_text):
    clear_screen()
    print("_" * 40)
    print(header_text)
    print("_" * 40)
