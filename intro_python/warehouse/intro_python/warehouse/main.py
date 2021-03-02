"""
name: Warehouse Management system
author: DeAndre Fuentes
functionlity:
    1 - register products

"""

# from menu import print_menu, clear_screen

from menu import *
from product import Product
import pickle


catalog = []
data_file = "warehouse.data"


def save_data(file_name):

    try:

        writer = open(file_name, "wb")  # wb = write binary data
        pickle.dump(catalog, writer)
        writer.close()
        print("** Data serialized!")
    except:

        print("** Error, data was not saved!!")


def load_data(file_name):

    try:

        reader = open(file_name, "rb")
        temp_list = pickle.load(reader)
        for prod in temp_list:
            catalog.append(prod)
        reader.close()

        print(f"** Loaded: {len(catalog)} products")

    except:
        print("** Error, file not found or not readable")
###################1##########################


def register_product():
    try:
        print_header("Register Product")
        title = input("please give title: ")
        category = input("give cat.: ")
        stock = int(input("give stock: "))
        price = float(input("give price: $"))
        select = ("Select an I.D. to Delete: ")

        next_id = 1
        if(len(catalog) > 0):
            next_id = catalog[-1].id + 1

        the_product = Product(next_id, title, category, stock, price)
        catalog.append(the_product)
        input("Product Created!")

    except ValueError:
        print("Error, Numbers only, Try again")

    except:
        print("**Error, try again!")


###################2##########################


def print_catalog(headerText="Your catalog"):
    print_header(headerText)

    for product in catalog:
        product.print()


###################3##########################


def report_no_stock():
    print_header("Report: products out of stock")

    for product in catalog:
        if(product.stock == 0):
            product.print()


###################4##########################


def report_stock_value():
    print_header("Report: Total stock Value")

    stock_value = 0.0
    for prod in catalog:
        total = prod.stock * prod.price
        stock_value += total

    print(f"Total stock value: {stock_value}")


###################5##########################


def report_cheapest_product():
    print_header("Report: cheapest Product")

    cheapest = catalog[0]
    for prod in catalog:
        if(prod.price < cheapest.price):
            cheapest = prod
    print("The cheapest product is:")
    cheapest.print()


###################6##########################


def delete_product():

    print_catalog("Delete a Product: ")
    id = int(input("please select a product "))

    found = False
    for prod in catalog:
        if(prod.id == id):
            found = True
            catalog.remove(prod)
            print(f"Product: {prod.id} - {prod.title} - has been Removed")

    if(not found):
        print("Error: Id invalid, try again")

###################7##########################


def update_price_stock():
    print_catalog("update - price - stock")

    id = int(input("select a product "))

    for prod in catalog:
        if(prod.id == id):
            new_price = float(input(" Enter the new price $"))
            new_stock = int(input("Enter the new stock "))

            prod.price = new_price
            prod.stock = new_stock

    """
   1. print catalog
   2. select id to update product
   3. find product 
   4. ask user for new price
   5. ask if user wants to update inventory 
   6. update products
   

    """


###################8##########################


def report_categories():
    print_header("Your categories")

    categories = []
    for prod in catalog:
        if(not prod.category in categories):
            categories.append(prod.category)
            print(prod.category)

    print(categories)


load_data(data_file)
input("Press enter to continue")


while(True):
    clear_screen()
    print_menu()

    opc = input("Please select an option")
    if(opc == "x"):
        break

    if(opc == "1"):
        register_product()
        save_data(data_file)

    elif(opc == "2"):
        print_catalog()

    elif(opc == "3"):
        report_no_stock()

    elif(opc == "4"):
        report_stock_value()

    elif(opc == "5"):
        report_cheapest_product()

    elif(opc == "6"):
        delete_product()

    elif(opc == "7"):
        update_price_stock()

    elif(opc == "8"):
        report_categories()

    input("Press enter to continue")


print("God bye!")
