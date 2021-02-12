drop database if exists recipes;
create database if not exists recipes;
use recipes;

create table recipe(
	recipe_id int auto_increment,
    recipe_name varchar(50) not null,
    primary key(recipe_id)
);

create table ingredient(
	ingredient_id int not null auto_increment,
    ingredient_name varchar(20) not null,
    primary key(ingredient_id)
);

create table recipe_ingredient(
	recipe_id int not null,
    ingredient_id int not null,
    persons_count int not null,
    quantity int not null,
    unit varchar(20) not null,
    primary key(recipe_id,ingredient_id,persons_count)
);

create table step_recipe(
	step_id int not null,
    recipe_id int not null,
    step_description longtext,
    primary key(step_id,recipe_id)
);