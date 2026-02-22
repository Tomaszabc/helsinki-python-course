def search_by_name(filename: str, word: str):
    with open(filename) as file:
        recipes_found_list = []
        for line in file:
            stripped_line = line.strip().lower()
            if word.lower() in stripped_line:
                recipes_found_list.append(line.strip())
        return recipes_found_list

def search_by_time(filename: str, prep_time: int):
    recipes_found = []

    with open(filename) as file:
        recipe_name = None
        recipe_time = None

        


def main():
    if False:
        recipes_file = input("recipes file: ")
    else:
        recipes_file = "recipes1.txt"
    # word = input("Recipe name: ")
    word = "cake"
    found_recipes = search_by_name(recipes_file, word)

    for recipe in found_recipes:
        print(recipe)
    prep_time = "20"
    found_recipes = search_by_time(recipes_file, prep_time)

    print(found_recipes)
        


main()