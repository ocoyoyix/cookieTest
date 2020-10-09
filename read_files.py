""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ2
Date: September 25, 2020 (functions are the same as PQ1 - Soup Recipes)
Description: This file holds the functions neccessary for reading the initial recipes files and creating recipe objects from those files. 
"""

import glob
import random
from classes import Recipe, Ingredient


def read_files(file_names, dict_ing_of_value):
    """Reads the file `recipes` and returns an array of Recipe objects 
    created from each file within `recipes`."""

    # Stores the final list of Recipes
    recipes_object_array = []

    # Loop through file_names (a file of files) and create
    # the Recipe objects and their accompanying
    # Ingredient array of objects
    for recipe_name in file_names:
        # Store the name of the recipe as a string
        recipe_string_name = recipe_name[8:-4]
        # print(recipe_name)

        # Open the current file and append each ingredient to the ingredient_array
        with open(recipe_name) as recipe:

            ingredient_array = []

            # Create the Ingredient objects
            for line in recipe:

                if (line.find(" g ") != -1):
                    ingredient_name = line.split(' g ')[1]
                    ingredient_name = ingredient_name.replace('\n', '')

                line_array = line.split()
                measurement = line_array[0]
                ingredient = create_ingredients(
                    ingredient_name, float(measurement), dict_ing_of_value)

                ingredient_array.append(ingredient)

            # Create the Recipe object
            recipe_object = create_recipe(recipe_string_name, ingredient_array)

            recipes_object_array.append(recipe_object)

    return (recipes_object_array)


def file_names(folder):
    """Returns the array of recipe names."""
    array_of_recipe_names = []

    for filename in glob.glob(folder):
        array_of_recipe_names.append(filename)
    return array_of_recipe_names


def create_recipe(recipe_name, ingredients):
    """Returns the new Recipe object."""
    recipe_created = Recipe(recipe_name, ingredients)
    return recipe_created


def create_ingredients(name, measurement, dict_ing_of_value):
    """Returns the new Ingredient object."""
    ingredient_created = Ingredient(name, measurement)

    # Add ingredient to INGREDIENTS_OF_VALUE
    if ingredient_created.name in dict_ing_of_value:
        dict_ing_of_value[ingredient_created.name] = dict_ing_of_value[ingredient_created.name] + [
            ingredient_created.amount]
    else:
        dict_ing_of_value[ingredient_created.name] = [
            ingredient_created.amount]

    ingredient_created.update_value(dict_ing_of_value)

    return ingredient_created

