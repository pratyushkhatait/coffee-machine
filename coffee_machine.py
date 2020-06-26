from beverage import Beverage
from singleton import singleton


@singleton
class CoffeeMachine:
    """
    Implementation of a Coffee Machine class
    """
    def __init__(self, N):
        """
        Initialize the coffee machine with given number(i.e. N) of outlets
        :param N:
        """
        self.outlets = N

    @staticmethod
    def get_beverage(bev_name, bev_ingredients):
        """
        This functions helps you get the beverage you have asked for.
        It will return True if the beverage is created successfully else False
        :param bev_name:
        :param bev_ingredients:
        :return: Boolean, message: Return a success/fail message
        """
        bev_obj = Beverage()
        success, item, reason = bev_obj.create_beverage(bev_ingredients)
        if success:
            response = "{} is prepared".format(bev_name)
        else:
            response = "{} can not be prepared because {} is {}".format(bev_name, item, reason)
        return success, response
