import yaml
import json

# Charger les données depuis le fichier JSON
with open('intents.json', 'r') as file:
    data = json.load(file)

# Créer une structure pour le fichier domain.yml
domain_data = {
    'intents': [],
    'responses': {}
}

# Traiter les intentions
for intent in data['intents']:
    domain_data['intents'].append({'name': intent['tag'], 'responses': [{'text': response} for response in intent['responses']]})
# Vérifier si les réponses sont dans une liste et reformatter si nécessaire
if isinstance(data['responses'], list):
    data['responses'] = {f"utter_{i}": [response] for i, response in enumerate(data['responses'], start=1)}

# Créer le fichier domain.yml
with open('domain.yml', 'w') as file:
    yaml.dump(domain_data, file, default_flow_style=False)
