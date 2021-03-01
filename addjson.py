import json



data_store = {'users':[{'Name': 'Jorge','steam_id': '6969696969'},{'Name':'steve'}]}
    #with open('path_to_file/person.json') as f:
        #data = json.load(f)
with open('C:\\Users\\salva\\PycharmProjects\\boolibot\\data.json', 'w') as json_file:
    json.dump(data_store, json_file)
    