import pprint
from json_api import JsonSncfApi

json_stop_areas = JsonSncfApi()
json_stop_areas.read_json_url()
areas = json_stop_areas.json_data

json_stop_areas.read_links()
links = json_stop_areas.list_hrefs
print(links)
#json_stop_areas.csv_export()
#list_href = json_stop_areas.get_last_key_value(areas,["links","href"])

"""# ajout d'un arrêt dans le json
entry = {
    'href': 'https://api.sncf.com/v1/coverage/sncf/stop_areas/{stop_areas.id}/test',
    'rel': 'stop_areas',
    'templated': True,
    'type': 'stop_areas'        
}
json_stop_areas.add_json_entry('stop_areas.json','links',entry)
pprint.pprint(json_stop_areas)"""

"""# affichage récurssif des clés du json
json_stop_areas.get_json_keys(areas)

# création d'une liste de champs à afficher
field_areas = ["id","name","codes","coord","administrative_regions"]

# création d'une liste contenant la liste des champs à afficher
# et la valeur de ces derniers ligne par ligne lorsqu'ils existent
row_areas = json_stop_areas.get_data_rows(field_areas,"stop_areas",areas)
row_links = json_stop_areas.get_data_rows(["href"],"links",areas)

# enregistrement des 2 listes dans des fichiers csv
json_stop_areas.csv_export("gares.csv",row_areas)
json_stop_areas.csv_export("links.csv",row_links)"""

"""# récupération des informations sur un trajet entre Paris Gare de Lyon et Lyon Perrache
# en utilisant la requête journey (blocage à ce niveau la)

# from Paris - Gare de Lyon
depart = "stop_area:OCE:SA:87686006"
# to Lyon - Perrache
arrival = "stop_area:OCE:SA:87722025"

# request journey
url = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrival}"
json_journeys = JsonApi(url,auth)
json_journeys.read_json_url()
json_journeys.save_json_url("journeys.json")
json_journeys.read_json("journeys.json")
journeys = json_journeys.json_data
pprint.pprint(journeys)

# combien y a-t-il d’arrêts entre ces deux gares ? (utilisez la clé ‘journeys’)
# clés -> journeys / sections / stop_date_time
il ya 2 arrêts entre ces 2 gares
"""