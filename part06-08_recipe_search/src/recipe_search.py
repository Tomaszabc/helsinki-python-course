def read_file(filename):
    with open(filename) as file:
        rows = []
        for row in file:
            rows.append(row.strip())
 
    recipes = []
    name_in_row = True
    prep_time_in_row = True
    new = { "ingredients": []}
    for row in rows:
        if name_in_row:
            new["name"] = row
            name_in_row = False
            prep_time_in_row = True
        elif prep_time_in_row:
            new["prep_time"] = int(row)
            prep_time_in_row = False
        elif len(row) > 0:
            new["ingredients"].append(row)
        else:
            recipes.append(new)
            name_in_row = True
            new = {"ingredients": []}
    recipes.append(new)
 
    return recipes
 
def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
 
    return found
 
def search_by_time(filename: str, time: int):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if recipe["prep_time"] <= time:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
 
def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
 
    found = []
    for recipe in recipes:
        if ingredient.lower() in recipe["ingredients"]:
            found.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
 
    return found
# def search_by_name(filename: str, word: str):
#     recipes_found_list = []
#     with open(filename) as file:
#         recipe_name = None
        
#         for line in file:
#             stripped = line.strip()

#             if stripped == "":
#                 if recipe_name and word.lower() in recipe_name.lower():
#                     recipes_found_list.append(recipe_name)
#                 recipe_name = None
#                 continue

#             if recipe_name is None:
#                 recipe_name = stripped
#             else:
#                 pass
        
#         if recipe_name and word.lower() in recipe_name.lower():
#             recipes_found_list.append(recipe_name)
#     return recipes_found_list
            

# def search_by_time(filename: str, prep_time: int):
#     recipes_found = []

#     with open(filename) as file:
#         recipe_name = None
#         recipe_time = None

#         for line in file:
#             stripped = line.strip()

#             if stripped == "":
#                 if recipe_name and recipe_time and recipe_time <= prep_time:
#                     recipes_found.append(f"{recipe_name}, preparation time {recipe_time} min")
                
#                 recipe_name = None
#                 recipe_time = None
#                 continue
#             if recipe_name is None:
#                     recipe_name = stripped
#             elif recipe_time is None:
#                 recipe_time = int(stripped)
#             else:
#                 pass
       
#         if recipe_name and recipe_time and recipe_time <= prep_time:
#                     recipes_found.append(f"{recipe_name}, preparation time {recipe_time} min")
#         return recipes_found

# def search_by_ingredient(filename: str, ingredient: str):
#     recipes_found = []

#     with open(filename) as file:
#         recipe_name = None 
#         recipe_time = None
#         ingredients = []

#         for line in file:
#             stripped = line.strip()

#             if stripped == "":
#                 if recipe_name and recipe_time and ingredient.lower() in ingredients:
#                     recipes_found.append(f"{recipe_name}, preparation time {recipe_time} min")

#                 recipe_name = None
#                 recipe_time = None
#                 ingredients = []
#                 continue

#             if recipe_name is None:
#                 recipe_name = stripped
#             elif recipe_time is None:
#                 recipe_time = int(stripped)
#             else:
#                 ingredients.append(stripped.lower())
#     if recipe_name and recipe_time and ingredient.lower() in ingredients:
#             recipes_found.append(f"{recipe_name}, preparation time {recipe_time} min")
    
#     return recipes_found


# def main():
#     if True:
#         recipes_file = input("recipes file: ")
#     else:
#         recipes_file = "recipes1.txt"
#     # word = input("Recipe name: ")
#     word = "cake"
#     found_recipes = search_by_name(recipes_file, word)

#     for recipe in found_recipes:
#         print(recipe)

#     prep_time = 20
#     found_recipes = search_by_time(recipes_file, prep_time)

#     for recipe in found_recipes:
#         print(recipe)

#     ingredient = "eggs"
#     found_recipes = search_by_ingredient(recipes_file, ingredient)
    
#     for recipe in found_recipes:
#         print(recipe)


