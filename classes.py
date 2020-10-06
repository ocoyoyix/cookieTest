""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ1
Date: September 25, 2020
Description: This file holds the Recipe and Ingredient classes used throughout this project. All of the methods are used within the other files in this project. 
"""


import random


class Recipe(object):
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        self.fitness = len(ingredients)
        self.curr_probability = 0
        self.total = 0

    def set_curr_prob(self, total):
        """Updates the probability of this recipe being chosen
        given the total fitness of all recipes in existence."""
        self.curr_probability = self.fitness/total

    def __str__(self):
        """Returns a string representation of this Recipe."""
        return f'Name: {self.name} Ingredients: {self.ingredients}'

    def print_ingredients(self):
        """Prints all of the ingredients for this Recipe."""
        for ingredient in self.ingredients:
            print(ingredient)

    def get_ingredient_names(self):
        """Prints all of the ingredient names (only) for this Recipe."""
        names_list = []
        for ingredient in self.ingredients:
            names_list.append(ingredient.name)
            print(ingredient.name)
        return names_list

    def get_toppings(self):
        """Returns the indexes of all the toppings in the recipe and all of the ingredient objects itself"""
        print("*in topping get*:")
        topping_list = [[], []]
        for i, ingredient in enumerate(self.ingredients):
            if '*' in ingredient.name:
                topping_list[0].append(i)
                topping_list[1].append(ingredient)
        return topping_list


class Ingredient(object):
    def __init__(self, name, amount, value=1):
        self.name = name
        self.amount = amount
        self.value = value

    def __str__(self):
        """Returns a string representation of this Ingredient."""
        return f"Ingredient: {self.name}, Amount: {self.amount}g, Value: {self.value}"

    def update_value(self, ingredients_of_val):
        amount_array = ingredients_of_val[self.name]
        length = len(amount_array)
        avg = 0
        for amount in amount_array:
            avg += amount
        avg = float(avg/length)
        amount = float(self.amount)
        print("average is : ",avg)
        print("amount is : ",amount)
        if amount == avg:
            self.value += 10
        elif amount > avg + 5 or amount < avg - 5:
            self.value -= 5
        elif amount > avg + 10 or amount > avg - 10:
            self.value -= 10
        
yuh = {
    "chips": [10, 40, 20],
    "egg": [2, 5]
}
ing = Ingredient("chips", 10)
a = ing.value
print(a)
ing.update_value(yuh)
a = ing.value
print(a)



# "ex. current ingredient is chips w/ 1 gram"

# INGREDIENTS_OF_VALUE["chips"] = [20, 30, 20,10]
# len = 4 
# avg = 20 
# + 80 perfect (=)
# - 20 slightly below avg (+/- 5)
# - 80 way below/above (+/- 6) """

