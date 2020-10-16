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
        self.fitness = 0
        self.current_probability = 0
        self.total = 0

    def set_current_prob(self, total):
        """Updates the probability of this recipe being chosen
        given the total fitness of all recipes in existence."""
        self.current_probability = self.fitness/total

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
        topping_list = [[], []]
        for i, ingredient in enumerate(self.ingredients):
            if '*' in ingredient.name:
                topping_list[0].append(i)
                topping_list[1].append(ingredient)
        return topping_list

    def set_fitness(self, ingredients_of_val):
        """Changes the fitness value of the recipe based on number toppings and number of ingredients."""
        total_fitness = 0

        for ingredient in self.ingredients:
            ingredient.update_value(ingredients_of_val)
            total_fitness += ingredient.value
        
        # Reduce the fitness of cookie recipes with no toppings 
        if(len(self.get_toppings()) == 0):
            total_fitness -= 45

        # Removes and Adds points based on lenfth of ingredients list
        if(len(self.ingredients) < 4):
            total_fitness -= 70
        elif(len(self.ingredients) >= 8):
            total_fitness += 20   
          
        self.fitness = total_fitness

    def remove_duplicates(self):
        """ Goes through the recipes and removes any dulucations that are found. """
        list_names = self.get_ingredient_names()
        
        for name in list_names:
            new_amount = 0.0 
            if(list_names.count(name) > 1):
                # find all indices of name 
                indicies = [i for i, ingredient in enumerate(self.ingredients) if ingredient.name == name]
                count = len(indicies) - 1
                while(len(indicies) != 1):
                    removed = self.ingredients.pop(indicies[count])
                    new_amount += removed.amount 
                    indicies.pop(count)
                    count -= 1
                self.ingredients[indicies[0]].amount += new_amount  

class Ingredient(object):
    def __init__(self, name, amount, value=1):
        self.name = name
        self.amount = amount
        self.value = value

    def __str__(self):
        """Returns a string representation of this Ingredient."""
        return f"Ingredient: {self.name}, Amount: {self.amount}g"

    def update_value(self, ingredients_of_val):
        """ Updates the value of the ingredient by using an avgerage based model to determine the value change"""
        amount_array = ingredients_of_val[self.name]
        length = len(amount_array)
        avg = 0
        for amount in amount_array:
            avg += amount
        avg = float(avg/length)
        amount = float(self.amount)

        self.value -= abs(avg - amount)
