# Coffee-Machine #
Implementation of a low level design of a coffee machine written in Python3 that serves beverages if the ingredients are available and sufficient. 
## Dependencies ##
-Python3

## main.py details ##
        # dictionary for options #
        opt = {
            1: "Initialize/Refill Ingredient's stock",
            2: "View all Ingredients in Stock",
            3: "Get beverage",
            4: "Exit"
        }

        print(" Menu:")
        print(" 1-Initialize/Refill Ingredient's stock\n 2-View all Ingredients in Stock\n 3-Get beverage\n 4-Exit\n")
        
        Select commands as above [1-4]
        Select input test cases which I have defined in inputs.py
        

## Trigger script (main.py) ##
1. python3 main.py
2. Select one number from [1-4] to execute a command from the above menu. For Ex:
3. I have created input test cases(i.e. input1, input2) in inputs.py. First select any of the test case here.
4. Select 1 to initialize the ingredient stock
5. Select 2 to check the list of all the ingredients present along with their quantity.
6. Select 3 to get beverages. Here you can see output message whether the requested beverage is prepared or not.
7. To quit Select 4.        