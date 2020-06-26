from ingredient import Ingredient


class Beverage:
    """
    This class defines/creates a beverage (i.e. tea, coffee etc.)
    """

    def __init__(self):
        """
        Since the ingredient class is a singleton class,
        so below code will return the instantiated object if any else create a new instance
        """
        self.ingredient_obj = Ingredient()

    def create_beverage(self, ingredients):
        """
        This functions helps in creating a beverage using the given ingredients.
        It returns False if the ingredient is either not available or it is not sufficient.
        :param ingredients: Provided ingredients with required quantity
        :return: Boolean, ingredient_name, reason
        """
        is_created, reason = True, ""

        for item, count in ingredients.items():
            if self.ingredient_obj.get_ingredient(item) == 0:
                is_created, reason = False, "not available"
                return is_created, item, reason
            elif self.ingredient_obj.get_ingredient(item) >= count:
                self.ingredient_obj.remove_ingredient(item, count)
            else:
                is_created, reason = False, "not sufficient"
                return is_created, item, reason

        return is_created, "", reason





