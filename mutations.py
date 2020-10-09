""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ1
Date: September 25, 2020
Description: This file includes a collection of functions that will either assist or cause mutations on given recipe objects 
"""

import random
from classes import Recipe, Ingredient


def ingredient_from_set(file_list, ingredient_names, amount=False):
    """Returns an ingredient from the inspiring set.A boolean is sent in the parameter to determine if we also need to change the ingredients amount"""
    # Finds the random file
    if(len(file_list) == 1):
        afile = file_list[0]
    else:
        afile = file_list[random.randint(0, (len(file_list)-1))]

    # This while loop ensures that the chosen ingredient from the i
    # nspiring set does not match an ingredient in the curent
    # list of ingredients
    while(True):
        # Chooses a random line from the random file
        lines = open(afile).read().splitlines()
        my_line = random.choice(lines)
        print(my_line)
        # ingredient_name = my_line.split(' g ')[1]
        if (my_line.find(" g ") != -1):
            ingredient_name = my_line.split(' g ')[1]
            ingredient_amount = my_line.split()[0]
        else:
            ingredient_name = " ".join(my_line.split()[1:])

        if(ingredient_names.count(ingredient_name) == 0):
            if (amount):
                return Ingredient(ingredient_name, ingredient_amount)
            else:
                return ingredient_name


def change_ingredient_amount(recipe_obj):
    """Changes the ingredient amount of a  random selected ingredient."""
    # gets a random ingredient to change
    ingredient = random.choice(recipe_obj.ingredients)

    previous_amount = ingredient.amount
    new_amount = random.randrange(1, 10)

    # this if statement makes sure that
    # there will always be a change in the amount
    if previous_amount == new_amount:
        new_amount += 1
    ingredient.amount = new_amount

    # Calculates the new total ounces of ingredients
    # in the recipe and then normalizes each quantity for
    # the final total to equal 100


def change_ingredient_name(recipe_obj, file_list):
    """An ingredient is selected uniformly at random from the recipe. 
    Its name is changed to that of another ingredient that is chosen at random 
    from the ones in the inspiring set."""
    ingredient = random.choice(recipe_obj.ingredients)
    new_name = ingredient_from_set(file_list, recipe_obj.ingredients)

    # This is where the ingredient name is changed
    while (ingredient.name == new_name):
        new_name = ingredient_from_set(file_list, recipe_obj.ingredients)
    
    ingredient.name = new_name

    # Calculates the new total ounces of ingredients
    # in the recipe and then normalizes each quantity for
    # the final total to equal 100


def change_topping(recipe_obj, file_list):
    """A topping is selected uniformly at random from the recipe. This topping is replaced with another random topping from the topping set"""
    existing_toppings = recipe_obj.get_toppings()[1]
    new_ing = ingredient_from_set(file_list, existing_toppings, True)
    if(len(recipe_obj.get_toppings()[0]) == 0):
        recipe_obj.ingredients.append(new_ing)
    else:
        index_to_change = random.choice(recipe_obj.get_toppings()[0])
        recipe_obj.ingredients[index_to_change] = new_ing


def add_ingredient(recipe_obj, file_list):
    """An ingredient is selected uniformly at random from the inspiring set 
    and added to the recipe."""
    ingredient_name = ingredient_from_set(file_list, recipe_obj.ingredients)

    # The amount of the new ingredient will be an int ,i, such that
    # 1<=1<10
    ingredient_amount = random.randrange(1, 10)
    recipe_obj.ingredients.append(
        Ingredient(ingredient_name, ingredient_amount))


def delete_ingredient(recipe_obj):
    """An ingredient is selected uniformly at random from the recipe, 
    and removed from the recipe."""

    # random ingredient index is chosen
    choose_ingredient = random.randint(0, len(recipe_obj.ingredients) - 1)

    # removes the ingredient from the recipe object
    recipe_obj.ingredients.pop(choose_ingredient)
