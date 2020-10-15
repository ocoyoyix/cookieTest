""" 
Authors: Orlando Coyoy, Ya'Kuana Davis, Roger Trejo
Course Name: CSCI 3725
Assignment Name: PQ1
Date: September 25, 2020
Description: This document can be used to run our modified version of PIERRE. The files classes.py, get_methods.py, reading_files.py and mutations are all imported into this file and utilized as necessary. Use `python3 main.py` in the terminal to explore our code.  
*** Disclaimer *** 
Sept. 25: change_ingredient_name function occasionally gets stuck in a loop. Recipe total amounts do not add up to 100. Some exceed and others are way below. 
Sept. 30: change_ingredient_name function has not broken the code after 30 runs. Recipe total amounts add up to 100. Decimal points can be 9 digits long. 
"""

import random
from read_files import read_files, file_names
from get_functions import pivot_ingredients, get_probability,  get_top_fitness
from mutations import add_ingredient, ingredient_from_set, delete_ingredient, change_ingredient_name, change_ingredient_amount, change_topping
from classes import Recipe, Ingredient


def main():
    INGREDIENTS_OF_VALUE = {}
    # prepping first generation from the inspiring set
    recipe_names = file_names("recipes/*.txt")
    topping_names = file_names("toppings/*.txt")
    parent = read_files(recipe_names, INGREDIENTS_OF_VALUE)
    
    for recipe in parent:
        recipe.remove_duplicates()
        recipe.set_fitness(INGREDIENTS_OF_VALUE)

    # creating n number of generations
    num_of_generations = 2
    num_of_offspring = 0

    # Each step in this outer for loop is the creation
    # of a new generation
    for x in range(1, num_of_generations+1):
        # final offspring list
        offspring_list = []

        # Each step in the inner for loop is creating a new Recipe for the offspring list
        for y in range(1, 7):
            # getting parent recipes
            two_recipes = get_probability(parent)

            # create the new ingredients list
            genetic_crossover = pivot_ingredients(
                two_recipes[0].ingredients, two_recipes[1].ingredients)

            num_of_offspring += 1
            name = "new_recipe_" + str(num_of_offspring)

            offspring = Recipe(name, genetic_crossover)
            recipe.remove_duplicates()

            # Chooses a random mutation method my asigning each function to an int int the range [0,3]
            generate_random_int = random.randint(0, 4)

            if (generate_random_int == 0):
                print("\n", "*** changing ingredient name ***")
                change_ingredient_name(offspring, recipe_names)
                offspring.remove_duplicates()
                offspring.set_fitness(INGREDIENTS_OF_VALUE)
            elif (generate_random_int == 1):
                print("\n", "*** changing ingredient amount ***")
                change_ingredient_amount(offspring)
                offspring.remove_duplicates()
                offspring.set_fitness(INGREDIENTS_OF_VALUE)
            elif (generate_random_int == 2):
                print("\n", "*** adding an ingredient ***")
                add_ingredient(offspring, recipe_names)
                offspring.remove_duplicates()
                offspring.set_fitness(INGREDIENTS_OF_VALUE)
            elif(generate_random_int == 3):
                print("\n", "*** deleting an ingredient ***")
                delete_ingredient(offspring)
                offspring.remove_duplicates()
                offspring.set_fitness(INGREDIENTS_OF_VALUE)

            offspring_list.append(offspring)

            print("\n", "----- current offspring list -----")
            for recipe in offspring_list:
                print("\n", recipe.name)


        # Create the final array of the 6 fittest Recipes
        for recipe in parent:
            recipe.remove_duplicates()
            recipe.set_fitness(INGREDIENTS_OF_VALUE)
        parent = get_top_fitness(offspring_list + parent)
        

        # Ranking fitnesses and getting the best recipe out of the parent recipes array
        best_recipe = parent[0]

    print("\n", "---------------------")
    print("\n", "* Final Recipes *")

    for recipe in parent:
        print("\n", recipe.name)
        recipe.print_ingredients()

    print("\n", "---------------------")
    print("\n", "* Top Recipe *")
    print(best_recipe.name)
    best_recipe.print_ingredients()

    print("--------------")
    print("ENJOY :)", "\n")


main()
