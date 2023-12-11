import json

# Charger les données depuis le fichier JSON
with open('intents.json', 'r') as json_file:
    data = json.load(json_file)

# Convertir les données en format YAML
yaml_data = "version: '3.0'\nnlu:\n"

for intent in data['intents']:
    tag = intent['tag']
    patterns = intent['patterns']

    # Créer la section pour chaque intention
    yaml_data += f"- intent: {tag}\n"
    yaml_data += "  examples: |\n"

    # Ajouter chaque exemple pour l'intention
    for pattern in patterns:
        yaml_data += f"    - {pattern}\n"

# Écrire les données dans un fichier YAML
with open('nlu.yml', 'w') as yaml_file:
    yaml_file.write(yaml_data)
