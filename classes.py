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

    def set_fitness(self):
        """Changes the fitness value of the recipe.It does so by adding the values of all the ingredients in the recipe"""
        total_fitness = 0
        for ingredient in self.ingredients:
            total_fitness += ingredient.value
        self.fitness = total_fitness


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
        if amount == avg:
            self.value += 10
        elif amount > avg + 5 or amount < avg - 5:
            self.value -= 5
        elif amount > avg + 10 or amount > avg - 10:
            self.value -= 10
