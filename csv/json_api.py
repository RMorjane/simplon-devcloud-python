import csv
import json
import requests
import pprint
import pandas

class JsonSncfApi:

    def __init__(self):
        self.url = "https://api.sncf.com/v1/coverage/sncf/stop_areas"
        self.headers = {"Authorization": 'b8d19b5e-f838-462b-9f30-334d98cd15a8'}
        self.json_filename = "stop_areas"
        self.csv_filename = ""
        self.json_data = {}
        self.list_keys = []
        self.list_hrefs = []
        self.data_rows = []

    def set_url(self,url):
        self.url = url
    
    def set_json_filename(self,json_filename):
        self.json_filename = json_filename

    def read_json_file(self):

        with open(self.json_filename + ".json", 'r') as f:
            data = f.read()
            self.json_data = json.loads(data)
            f.close()

    def read_json_url(self):

        response = requests.get(self.url,headers = self.headers)
        if response.status_code == 200:
            self.json_data = json.loads(response.text)
            json.dumps(self.json_data, indent=2)
        else:
            print("Erreur de connexion")

    def save_json(self):

        with open(self.json_filename + ".json", 'w') as f:   
            #json.dump(self.json_data,f)
            f.write(json.dumps(self.json_data, indent=4))
            f.close()

    def add_json_entry(self,key,entry):

        with open(self.json_filename + ".json") as f:
            self.json_data = json.load(f)
            self.json_data[key].append(entry)
        self.save_json()

    def get_data_rows(self,fieldnames,key,data):
        # création d'une liste avec la liste des champs à afficher comme premier élémént
        self.data_rows = [fieldnames]
        if type(self.json_data)==dict:
            if type(self.json_data[key])==list:
                for field in fieldnames:
                    # création d'une liste contenant les valeurs de chaque champ (field)
                    rows = [loop_data[field] for loop_data in self.json_data[key] if field in loop_data.keys()]
                    i = 0
                    for item in rows:
                        i += 1
                        try: # si la valeur du data_row[i] existe
                            self.data_rows[i].append(item)
                        except: # sinon on crée une nouvelle liste contenant la valeur du champs à afficher
                            self.data_rows.append([item])

    def read_links(self):
        self.get_key_values("href",self.json_data)
        self.list_hrefs = self.list_keys
        self.get_data_rows(["href"],"links",self.json_data)
        self.csv_filename = "links"

    def csv_export(self):   
        # création du fichier csv
        with open(self.csv_filename + ".csv",mode="w",newline='') as f:
            # newline='' pour éliminer les lignes vides du fichier csv
            csv_writer = csv.writer(f,delimiter=';')
            if type(self.data_rows)==list:
                for row in self.data_rows:
                    # écriture du contenu du row dans la nouvelle ligne du fichier csv
                    csv_writer.writerow(row)
            f.close()

    # fonction permettant d'afficher l'arborescence des clés du json data
    def get_json_keys(self,data,i=0):
        i += 1
        if type(data) == dict:
            for key,value in dict(data).items():
                print("    "*(i-1)+"|---->",key,"(dict)")
                self.get_json_keys(value,i)
        elif type(data) == list:
            for loop_data in list(data):
                self.get_json_keys(loop_data,i)

    # fonction qui permet de récupérer la liste des valeurs d'une clé dans le json
    def get_key_values(self,local_key,data):
        if type(data) == dict:
            for key,value in dict(data).items():
                if key == local_key:
                    self.list_keys.append(value)
                else:
                    self.get_key_values(local_key,value)
        elif type(data) == list:
            for loop_data in list(data):
                self.get_key_values(local_key,loop_data)

    def read_csv(self):
        output = pandas.read_csv(self.csv_filename + ".csv",sep=';',index_col=0)
        print(output)