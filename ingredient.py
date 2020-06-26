from collections import defaultdict
from singleton import singleton


@singleton
class Ingredient:
    """
    This is a Singleton Ingredient class which provide details (like stock) of all the ingredients in this machine
    """

    def __init__(self):
        """
        Constructor that initializes a default dictionary to store ingredient details
        """
        self._ingredient = defaultdict(int)

    def get_ingredient(self, item):
        """
        Get stock count of a given ingredient.
        :param item: ingredient
        :return: quantity of the ingredient
        """
        return self._ingredient[item]

    def set_ingredient(self, ingredients):
        """
        Update(add/initialize) the ingredient stock.
        :param ingredients: all the given ingredients
        :return:
        """
        for ing, quantity in ingredients.items():
            self._ingredient[ing] += quantity

    def remove_ingredient(self, item, count):
        """
        Remove the given ingredient count by given quantity
        :param item: Given ingredient that needs to be removed
        :param count: remove by quantity=count
        :return:
        """
        self._ingredient[item] -= count

    def show_all_ingredient(self):
        """
        Returns the ingredient dictionary that contains all the ingredients details
        :return: ingredient dictionary
        """
        return self._ingredient

