import time
from coffee_machine import CoffeeMachine
from ingredient import Ingredient
from inputs import input1, input2


# Initialize/Refill ingredient's stock
def update_stock(stocks):
    """
    This function initializes/refills ingredient's stock
    :param stocks: ingredient's quantity
    :return: None
    """
    ingredient = Ingredient()
    ingredient.set_ingredient(stocks)
    print("------------------------------------------")
    print("Successfully updated the stock")
    print("------------------------------------------")


# Show all ingredients
def show_ingredients():
    """
    This function show all the ingredients present in the Coffee Machine
    :return:
    """
    ingredient = Ingredient()
    ingredients = ingredient.show_all_ingredient()
    print("------------------------------------------")
    if not ingredients:
        print("Currently No ingredient is available!")
    else:
        print("List of ingredients:")
        for ing, quantity in ingredients.items():
            print("{}:  {}".format(ing, quantity))
    print("------------------------------------------")


# Get your beverages
def get_my_beverage(outlets, selected_beverages):
    """
    This functions helps you get your beverages.

    Logic of this function is:

    At any given point, the number of maximum beverages served by machine should be <= # of outlets in the machine.
    My assumptions:
    If all the ingredients for a given beverage are available and all the outlets are running then,
    user have to wait for 5 seconds to place next order.
    But if any ingredient is not sufficient or not available for a particular ordered beverage,
    then I do not count that outlet to be busy, that means next order can be served at that time immediately.

    :param outlets: # of outlets in the machine
    :param selected_beverages: Beverages you have selected
    :return: str: Whether you get your beverage successfully or not
    """
    print("------------------------------------------")

    machine = CoffeeMachine(outlets)
    current_running_outlet = 0
    for bev_name, bev_ingredients in selected_beverages.items():
        if current_running_outlet >= outlets:
            print("*****Only {} beverages can be served at a time. Please wait for 5 seconds**********".format(outlets))
            time.sleep(5)
            current_running_outlet = 0
        status, output = machine.get_beverage(bev_name, bev_ingredients)
        if status:
            current_running_outlet += 1
        print(output)

    print("------------------------------------------")


if __name__ == "__main__":

    while True:
        # dictionary for options
        opt = {
            1: "Initialize/Refill Ingredient's stock",
            2: "View all Ingredients in Stock",
            3: "Get beverage",
            4: "Exit"
        }

        print(" Menu:")
        print(" 1-Initialize/Refill Ingredient's stock\n 2-View all Ingredients in Stock\n 3-Get beverage\n 4-Exit\n")

        try:
            n = int(input("Enter an option to opt for: "))
        except ValueError:
            print("***********Invalid input. Try again....*************")
            continue

        # Select input test case from inputs file to get the user's beverage requirement
        input_test = input2

        # Parse input dictionary
        total_outlets = input_test["machine"]["outlets"]["count_n"]
        stocks = input_test["machine"]["total_items_quantity"]
        beverages = input_test["machine"]["beverages"]

        if n == 1:
            update_stock(stocks)
        elif n == 2:
            show_ingredients()
        elif n == 3:
            get_my_beverage(total_outlets, beverages)
        elif n == 4:
            print("************It was our pleasure serving you. Visit Again........***********")
            exit(0)
        else:
            print("******Invalid input, Try again........*********")
            continue
