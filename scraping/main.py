import pprint
from recipe import RecipeInfo,MySQLReceip

def main():

    url_recipe = "https://www.atelierdeschefs.fr/fr/recette/4929-pate-a-crepe-facile.php"

    recipe = RecipeInfo(url_recipe)

    recipe.read_soup()
    recipe.read_recipe_name()
    recipe.read_persons_count()
    recipe.read_ingredients_infos()
    recipe.read_steps_infos()

    print(recipe.recipe_name)
    print("persons count : %d" % recipe.persons_count)
    print("ingredients infos : ")
    pprint.pprint(recipe.list_ingredients)
    pprint.pprint(recipe.list_steps)

    mysql_recipe = MySQLReceip()
    mysql_recipe.connect()
    mysql_recipe.add_recipe(recipe)

if __name__ == '__main__':
    main()