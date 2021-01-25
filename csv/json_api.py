import csv
import json
import requests
import pprint




def get_json_data(json_file):
    json_data = None
    with open(json_file, 'r') as f:
        data = f.read()
        json_data = json.loads(data)
        f.close()
    return json_data




def dump_json_data(json_file,key,entry):

    json_data = None

    with open(json_file) as f:
        json_data = json.load(f)
        json_data[key].append(entry)
        
    with open(json_file, 'w') as f:   
        json.dump(json_data,f)
        #f.write(json.dumps(json_data, indent=2))
        f.close()
    
    return json_data




# affichage du fichier json avec le module prettyprint
def display_json_file():
    json_data = get_json_data('stop_areas.json')
    pprint.pprint(json_data)




# ajout d'un arrêt dans le json
def add_json_entry():

    entry = {
        'href': 'https://api.sncf.com/v1/coverage/sncf/stop_areas/{stop_areas.id}/test',
        'rel': 'stop_areas',
        'templated': True,
        'type': 'stop_areas'        
    }

    json_data = dump_json_data('stop_areas.json','links',entry)
    pprint.pprint(json_data)


def get_json_data_url(url,headers):

    response = requests.get(url,headers = headers)

    if response.status_code == 200: # HTTP 200 OK
        json_data = json.loads(response.text)
        json.dumps(json_data, indent=2)
        return json_data
    else:
        return None

def cvs_export(filepath,data_rows):   
    # création du fichier csv
    with open(filepath,mode="w",newline='') as f:
        # newline='' pour éliminer les lignes vides du fichier csv
        csv_writer = csv.writer(f,delimiter=';')
        if type(data_rows)==list:
            for row in data_rows:
                # écriture du contenu du row dans la nouvelle ligne du fichier csv
                csv_writer.writerow(row)
        f.close()

def get_data_rows(fieldnames,key,data):
    # création d'une liste avec la liste des champs à afficher comme premier élémént
    data_rows = [fieldnames]
    if type(data)==dict:
        if type(data[key])==list:
            for field in fieldnames:
                # création d'une liste contenant les valeurs de chaque champ (field)
                rows = [loop_data[field] for loop_data in data[key] if field in loop_data.keys()]
                i = 0
                for item in rows:
                    i += 1
                    try: # si la valeur du data_row[i] existe
                        data_rows[i].append(item)
                    except: # sinon on crée une nouvelle liste contenant la valeur du champs à afficher
                        data_rows.append([item])
    
    return data_rows

def main():

    # requeter une api avec le module requests
    url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
    headers = {"Authorization": 'b8d19b5e-f838-462b-9f30-334d98cd15a8'}
    
    # récupération des données au format json
    json_data = get_json_data_url(url,headers)
    print(type(json_data))

    # création d'une liste de champs à afficher
    field_areas = ["id","name","codes","coord","administrative_regions"]

    # création d'une liste contenant la liste des champs à afficher
    # et la valeur de ces derniers ligne par ligne lorsqu'ils existent
    data_areas = get_data_rows(field_areas,"stop_areas",json_data)

    # enregistrement de cette liste dans un fichier gares.csv
    cvs_export("gares.csv",data_areas)

    """# récupération des informations sur un trajet entre Paris Gare de Lyon et Lyon Perrache
    # en utilisant la requête journey (blocage à ce niveau la)

    # from Paris - Gare de Lyon
    depart = "stop_area:OCE:SA:87686006"
    # to Lyon - Perrache
    arrival = "stop_area:OCE:SA:87722025"

    # request journey
    url = f"https://api.sncf.com/v1/journeys?from={depart}&to={arrival}"
    json_journeys = get_json_data_url(url,headers)
    print(type(json_journeys))
    #pprint.pprint(json_journeys)

    # combien y a-t-il d’arrêts entre ces deux gares ? (utilisez la clé ‘journeys’)
    #fieldnames = ["journeys","sections","stop_date_times","stop_point","label"]
    data_journeys = json_journeys["journeys"]
    print(type(data_journeys))
    print(len(data_journeys))

    if type(data_journeys) == list:
        for loop_data_journeys in data_journeys:
            print(type(loop_data_journeys))
            if type(loop_data_journeys) == dict:
                if "sections" in loop_data_journeys:
                    print(len(loop_data_journeys["sections"]))
                    print(type(loop_data_journeys["sections"]))
                    if type(loop_data_journeys["sections"]) == list:
                        for loop_sections in loop_data_journeys["sections"]:
                            print(type(loop_sections))"""

main()