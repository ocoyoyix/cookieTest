# CookieRecipeGenerator2020
Bowdoin College CSCI 3725 PQ2 

# Collaborators 
- Roger Trejo 
- Orlando Coyoy
- Ya'Kuana Davis

# Description
The main purpose of this project is to use an inspiring set of cookie recipes and create a program that builds new recipes based off this inspiring set. In this project we use chocolate chip recipes from four three different websites that we determined to be great cookie recipes. The cookie generator combines, adds, and removes different ingredients from each recipe in order to create a new and improved chocolate chip recipe. The name of our cookie generator is GenC2020.  

# Computational Creativity 
- [ ] Random - mutations & recipe creation 
    Our five mutations have equal probability of occuring and altering a newly generated recipe in their respective ways. Our recipe creation is also random as the ingredients from the parent recipe are selected at random using a pivot.
- [ ] Memorization - storing inspiring set 
    Our systems uses the inspiring set as a bases for all of the furture generated cookies. Ingredients within the inspiring set become our system's bias and influence the types of cookies generated. This was very important for metrics as our system needed a way to keep important aspects of a cookie(the foundation/cookie dough and the topping), and it was not doing so before we included the dictionary that stored averages of valuable ingredients. 
- [ ] Filter - fitness 
    Our system uses a ranking sytem that adds value to certain ingredients and deducts value for certain amounts of ingredients. Some ingredients and toppings are rewarded more fitness points and other deduct from a recipes fitness value. Without this filter, almost every recipe did not make any sense. Once we adjusted our values, the recipes were more likley to produce something novel that could also be applied realistically.

# Setup
In this project there is already a given inspiring set, but if there are other chocolate chip recipes that want to be used, simply replacing the current inspiring set and making sure the syntax and measurements are equivalent, can work as well. 

Next would be to simply run the program through the main.py file and watch as the cookie generator uses the inspiring set to make even better and tastier chocolate chip cookies!

# Insiring Set Recipes 

- https://www.epicurious.com/
- https://sallysbakingaddiction.com/
- 
