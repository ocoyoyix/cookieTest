""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ1
Date: September 25, 2020
Description: This file holds three functions. get_probability() generates and return a new recipe object based on the best of a given set. get_top_fitness() returns the top three recipes in a given list based on its fitness. Both methods are useful for generating the new recipes and new generations in the main.py file. pivot_ingredients() Returns the combination of two lists after they have each been split by a random pivot
"""
from classes import Recipe, Ingredient
import random

TOTAL_FITNESS = 0.0


def get_probability(recipes_array):
    """Returns two recipes at random which will be used to create a new recipe"""
    global TOTAL_FITNESS

    greatest_prob = 0.0

    # get the total number of ingredients
    for recipe in recipes_array:
        TOTAL_FITNESS += recipe.fitness

    # update the probability of each recipe being chosen
    for recipe in recipes_array:
        recipe.set_current_prob(TOTAL_FITNESS)

        if recipe.current_probability > greatest_prob:
            greatest_prob = recipe.current_probability

    # store propability selected recipes without duplicates
    selected = set()
    found = True

    while (found):
        random_num = random.uniform(0, greatest_prob)

        for recipe in recipes_array:
            if recipe.current_probability < random_num:
                selected.add(recipe)

        if len(selected) >= 2:
            found = False

    # final two recipes to make new soup
    final = []
    selected = list(selected)

    if len(selected) != 2:
        first = selected[0]
        second = selected[1]

        # take the two with the highest fitness ranking
        for recipe in selected:
            if recipe.fitness >= first.fitness:
                first = recipe
            elif recipe.fitness >= second.fitness:
                second = recipe
        final.append(first)
        final.append(second)
    else:
        final = selected

    return final


def pivot_ingredients(list_one, list_two):
    """Returns the combination of two lists after they have each been split by a random pivot"""

    # These if statements handle the cases where a
    # list is of length equal to or less than one.
    # In this case a randomint can not be found so
    # the pivot is default to 0
    ingredientName_array = []
    ingredient_array = []

    if len(list_one) <= 1:
        pivot_one = 0
    else:
        pivot_one = random.randint(0, len(list_one) - 1)

    if len(list_two) <= 1:
        pivot_two = 0
    else:
        pivot_two = random.randint(0, len(list_two) - 1)

    # Combines the new lists by their pivot
    newList = list_one[0:pivot_one] + list_two[pivot_two:]
    newList = list(set(newList))

    # Makes sure no repition of ingredients occurs in the list returned
    for ingredient in newList:
        if not (ingredient.name in ingredientName_array):
            ingredient_array.append(ingredient)
            ingredientName_array.append(ingredient.name)
    return ingredient_array


def get_top_fitness(recipes_array):
    """Returns a list of the top 6 ranked"""

    fitness_array = []
    top_ranked_ordered = []
    top6_array = []

    for recipe in recipes_array:
        fitness = recipe.fitness
        fitness_array.append(fitness)

    fitness_array.sort(reverse=True)
    fitness_array = fitness_array[:6]

    for recipe in recipes_array:
        if recipe.fitness in fitness_array:
            top6_array.append(recipe)

    count = 0
    while (count < 6):
        first = max(fitness_array)
        for recipe in top6_array:
            if recipe.fitness == first:
                top_ranked_ordered.append(recipe)
                count += 1
                fitness_array.remove(first)
                if len(fitness_array) == 0:
                    break
            first = max(fitness_array)
    return top_ranked_ordered
