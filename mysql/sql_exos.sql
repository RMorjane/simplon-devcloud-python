/* Q1 : Obtenir la liste des 10 villes les plus peuplées en 2012 */
select ville_nom,ville_population_2012
from villes_tests.villes_france_free
group by ville_nom
order by ville_population_2012
desc limit 10;

/* Q2 : Obtenir la liste des 50 villes ayant la plus faible superficie */
select ville_nom, ville_surface
from villes_tests.villes_france_free
group by ville_nom
order by ville_surface asc
limit 50;

/* Q3 : Obtenir la liste des départements d’outres-mer, c’est-à-dire ceux dont le
numéro de département commencent par “97” */
select departement_code, departement_nom
from villes_fr.departement
where departement_code like '97%';

/* Q4 : Obtenir le nom des 10 villes les plus peuplées en 2012, ainsi que le nom
du département associé */
select ville_nom,ville_population_2012,departement_nom
from villes_tests.villes_france_free, villes_fr.departement
where ville_departement = departement_code
group by ville_nom
order by ville_population_2012
desc limit 10;

/* Q5 : Obtenir la liste du nom de chaque département, associé à son code et du
nombre de commune au sein de ces département, en triant afin d’obtenir
en priorité les départements qui possèdent le plus de communes */
select departement_code, departement_nom, count(ville_commune) as nbr_commune
from villes_fr.departement, villes_tests.villes_france_free
where departement_code = ville_departement
group by departement_code
order by nbr_commune desc;

/* Q6 : Obtenir la liste des 10 plus grands départements, en terme de superficie */
select departement_code, departement_nom, ville_surface
from villes_fr.departement, villes_tests.villes_france_free
where departement_code = ville_departement
group by departement_code
order by ville_surface desc
limit 10;

/* Q7 : Compter le nombre de villes dont le nom commence par “Saint” */
select count(ville_nom_reel) as `nombre de villes commencant par Saint`
from villes_tests.villes_france_free
where ville_nom like 'Saint%';

/* Q8 : Obtenir la liste des villes qui ont un nom existants plusieurs fois, et trier
afin d’obtenir en premier celles dont le nom est le plus souvent utilisé par
plusieurs communes */
select ville_nom_reel, count(ville_commune) as nbr_commune
from villes_tests.villes_france_free
group by ville_nom_reel
order by nbr_commune desc;

/* Q9 : Obtenir en une seule requête SQL la liste des villes dont la superficie est
supérieur à la superficie moyenne */
select ville_nom_reel, ville_surface
from villes_tests.villes_france_free
where ville_surface > (select avg(ville_surface) from villes_tests.villes_france_free)
group by ville_nom_reel;