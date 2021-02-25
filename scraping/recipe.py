import requests
import pprint
import mysql.connector
from bs4 import BeautifulSoup

class RecipeCategory:

    def __init__(self,url):
        self.url = url
        self.recipe_category_name = ""
        self.links = []

    def read_infos(self):
        response = requests.get(self.url)
        encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
        soup = BeautifulSoup(response.content, from_encoding=encoding,features="html.parser")
        self.recipe_category_name = " ".join(soup.find("h1").string.split())
        self.links = [
            {
                "recipe_name": loop_link["title"],
                "href": loop_link["href"]
            }
            for loop_link in soup.find_all("a",{"class": "recipe-name"},href=True)        
        ]

    def display(self):
        print("%s : " %self.recipe_category_name)
        for loop_link in self.links:
            print(loop_link)

    def save_mysql_recipe(self):
        mysql_recipe = MySQLRecipe()
        mysql_recipe.connect()
        for loop_link in self.links:
            print(loop_link["href"])
            recipe_info = RecipeInfo(loop_link["href"])
            recipe_info.read_infos()
        mysql_recipe.connection.close()

class RecipeInfo:

    def __init__(self,href):
        self.url = "https://www.atelierdeschefs.fr" + href
        self.recipe_name = ""
        self.persons_count = 0
        self.list_usages = []
        self.list_ingredients = []
        self.list_steps = []

    def read_infos(self):
        response = requests.get(self.url)
        encoding = response.encoding if 'charset' in response.headers.get('content-type', '').lower() else None
        soup = BeautifulSoup(response.content, from_encoding=encoding,features="html.parser")
        self.recipe_name = soup.find("h1").string
        self.persons_count = int(soup.find("option",{"class": "yield"}).string)
        self.list_usages = [loop_usage.string for loop_usage in soup.find_all("li",{"class": "bold marginT10"})]
        print(self.list_usages)

        mysql_recipe = MySQLRecipe()
        mysql_recipe.connect()
        cursor = mysql_recipe.connection.cursor()

        add_recipe = "INSERT INTO recipe(recipe_name,recipe_url) values('{0}','{1}')".format(self.recipe_name,self.url)
        cursor.execute(add_recipe)
        mysql_recipe.connection.commit()
        recipe_id = cursor.lastrowid

        usage = "ingredient"

        list_li = soup.find_all("li")
        for k in list_li:
            k_childs = k.findChildren()
            if len(k_childs)==2 and k_childs[0].name=="span" and k_childs[1].name=="span":
                final_index = len(k_childs[0].text)-3
                list_quantity = k_childs[1].text.split(' ')

                add_usage = "INSERT INTO ingredient_usage(usage_name) values(%s)"
                cursor.execute(add_usage,(usage,))
                mysql_recipe.connection.commit()
                usage_id = cursor.lastrowid

                ingredient = " ".join(k_childs[0].text.strip()[0:final_index].split())

                add_ingredient = "INSERT INTO ingredient(ingredient_name) values(%s)"
                cursor.execute(add_ingredient,(ingredient,))
                mysql_recipe.connection.commit()
                ingredient_id = cursor.lastrowid

                try:
                    quantity = int(list_quantity[0])
                except:
                    quantity = float(list_quantity[0])

                unit = list_quantity[1]

                add_recipe_ingredient = """
                    INSERT INTO recipe_ingredient(recipe_id,ingredient_id,usage_id,persons_count,quantity,unit)
                    values(%s,%s,%s,%s,%s,%s)
                """
                cursor.execute(add_recipe_ingredient,(recipe_id,ingredient_id,usage_id,self.persons_count,quantity,unit))
                mysql_recipe.connection.commit()

                self.list_ingredients.append(
                    {
                        "usage": usage,
                        "ingredient": ingredient,
                        "quantity": quantity,
                        "unit": unit
                    }
                )

            elif k.text in self.list_usages:
                usage = k.text

        steps_name = [step.string for step in soup.find_all("span",{"class": "bold"}) if ". POUR " in step.string]
        steps_description = soup.find_all("p",{"class": "marginT10 fz110 lh120"})
        steps_count = len(steps_name)
        for i in range(steps_count):
            order = steps_name[i]
            description = steps_description[i].text.replace("\r\n"," ").replace("\n","")
            add_step = """insert into step_recipe(step_name,recipe_id,step_description)
                        values('{0}',{1},'{2}');""".format(
                            order.replace("'","\\'"),
                            recipe_id,
                            description.replace("'","\\'")
                        )
            cursor.execute(add_step)
            mysql_recipe.connection.commit()
            
            self.list_steps.append(
                {
                    "order": order,
                    "description": description
                }
            )
        cursor.close()

    def display(self):
        print(self.recipe_name)
        pprint.pprint(self.list_ingredients)
        pprint.pprint(self.list_steps)

class MySQLRecipe:

    def __init__(self):
        self.hostname = "localhost"
        self.username = "root"
        self.password = "Oumaima1*"
        self.database = "recipes"
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.hostname,
            user=self.username,
            passwd=self.password,
            database=self.database
        )
        print(self.connection)

    def create_database(self):
        cursor = self.connection.cursor()
        create_db = """
            drop database if exists recipes;
            create database if not exists recipes;
            use recipes;

            create table recipe(
                recipe_id int auto_increment,
                recipe_name varchar(100) not null,
                recipe_url varchar(200) not null,	
                primary key(recipe_id)
            );

            create table ingredient(
                ingredient_id int not null auto_increment,
                ingredient_name varchar(50) not null,
                primary key(ingredient_id)
            );

            create table ingredient_usage(
                usage_id int not null auto_increment,
                usage_name varchar(50) not null,
                primary key(usage_id)
            );

            create table recipe_ingredient(
                recipe_id int not null,
                ingredient_id int not null,
                usage_id int not null,
                persons_count int not null,
                quantity int not null,
                unit varchar(20) not null,
                primary key(recipe_id,ingredient_id,usage_id,persons_count)
            );

            create table step_recipe(
                step_name varchar(50) not null,
                recipe_id int not null,
                step_description longtext,
                primary key(step_name,recipe_id)
            );
        """
        cursor.execute(create_db,multi=True)