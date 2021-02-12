import requests
import mysql.connector
from bs4 import BeautifulSoup

class RecipeInfo:

    def __init__(self,url):
        self.url = url
        self.soup = None
        self.recipe_name = None
        self.persons_count = 0
        self.list_ingredients = []
        self.list_steps = []

    def read_soup(self):
        response = requests.get(self.url)
        page = response.content
        self.soup = BeautifulSoup(page)

    def read_recipe_name(self):
        self.recipe_name = self.soup.find("h1").string

    def read_persons_count(self):
        self.persons_count = int(self.soup.find("option",{"class": "yield"}).string)

    def read_ingredients_infos(self):
        ingredients = self.soup.find_all("span",{"class": "ingredient"})
        quantities = self.soup.find_all("span",{"class": "quantite bold"})
        list_count = len(ingredients) 
        for i in range(list_count):
            list_quantity = quantities[i].string.split(' ')
            final_index = len(ingredients[i].string)-3
            self.list_ingredients.append(
                {
                    "ingredient": ingredients[i].string.strip()[0:final_index],
                    "quantity": int(list_quantity[0]),
                    "unit": list_quantity[1]
                }
            )

    def read_steps_infos(self):
        steps = self.soup.find_all("p",{"class": "marginT10 fz110 lh120"})
        steps_count = len(steps)
        for i in range(steps_count):
            self.list_steps.append(
                {
                    "order": i+1,
                    "description": steps[i].string.strip()
                }
            )

class MySQLReceip:

    def __init__(self):
        self.hostname = "mysql-server"
        self.username = "root"
        self.password = "Oumaima1*"
        self.database = "recipes"
        self.connection = None
        self.cursor = 0
      
    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.hostname,
            user=self.username,
            passwd=self.password,
            database=self.database
        )
        print(self.connection)

    def create_database(self):
        self.cursor.execute("source recipes.sql;")

    def add_recipe(self,recipe_info):
        if type(recipe_info)==RecipeInfo:
            print(recipe_info.recipe_name)
            insert_recipe = "insert into recipe(recipe_name) values({0});".format("'"+recipe_info.recipe_name+"'")
            insert_ingredients = []
            for loop_ingredient in recipe_info.list_ingredients:
                insert_ingredients.append(
                    "insert into ingredient(ingredient_name) values({0});".format("'"+loop_ingredient["ingredient"]+"'")
                )
            self.cursor = self.connection.cursor()
            self.cursor.execute(insert_recipe)
            self.connection.commit()
            self.connection.close()
        else:
            print("The variable recipe_info is not a RecipeInfo instance")