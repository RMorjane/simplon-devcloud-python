# import du module pprint et de la classe JSonSncfApi
import pprint
from json_api import JsonSncfApi

"""# récupération du json
json_stop_areas = JsonSncfApi()
json_stop_areas.read_json_url()
areas = json_stop_areas.json_data

# affichage du json en utilisant le module pretty print
pprint.pprint(areas)

# lecture et affichage de la liste des liens href du json
json_stop_areas.read_links()
links = json_stop_areas.list_hrefs
print(links)

# enregistrement de cette liste dans un fichier csv
json_stop_areas.csv_export()

# ajout d'un arrêt dans le json
entry = {
    'href': 'https://api.sncf.com/v1/coverage/sncf/stop_areas/{stop_areas.id}/test',
    'rel': 'stop_areas',
    'templated': True,
    'type': 'stop_areas'        
}
json_stop_areas.add_json_entry('links',entry)
pprint.pprint(json_stop_areas)

# affichage récurssif des clés du json
json_stop_areas.get_json_keys(areas)

# création d'une liste de champs à afficher
field_areas = ["id","name","codes","coord","administrative_regions"]

# création d'une liste contenant la liste des champs à afficher
# et la valeur de ces derniers ligne par ligne lorsqu'ils existent
json_stop_areas.get_data_rows(field_areas,"stop_areas",areas)
row_areas = json_stop_areas.data_rows

# enregistrement de la liste des informations des gares dans un fichier gares.csv
json_stop_areas.set_csv_filename("gares")
json_stop_areas.csv_export()"""

# récupération des informations sur un trajet entre Paris Gare de Lyon et Lyon Perrache
# en utilisant la requête journey (blocage à ce niveau la)

# from Paris - Gare de Lyon
depart = "stop_area:OCE:SA:87686006"
# to Lyon - Perrache
arrival = "stop_area:OCE:SA:87722025"

# request journey
url = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrival}"
json_journeys = JsonSncfApi()
json_journeys.set_url(url)
json_journeys.set_json_filename("journeys")
json_journeys.set_csv_filename("journeys")
json_journeys.read_json_url()
json_journeys.save_json()
journeys = json_journeys.json_data

#json_journeys.get_json_keys(journeys["journeys"][0]["sections"][1]["stop_date_times"])
json_journeys.get_key_values("label",journeys["journeys"][0]["sections"][1]["stop_date_times"])
stop_areas = json_journeys.list_keys
pprint.pprint(stop_areas)

json_journeys.get_key_values("stop_date_times",journeys)
stop_date_times = json_journeys.list_keys
for area in stop_date_times[0]:
    print("Gare : ",area["stop_point"]["name"],"Départ : ",area["departure_date_time"],"Arrivée : ",area["arrival_date_time"])

# combien y a-t-il d’arrêts entre ces deux gares ? (utilisez la clé ‘journeys’)
# clés -> journeys / sections / stop_date_time
# il ya 2 arrêts entre ces 2 gares
