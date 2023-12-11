import json
import yaml

# Charger les données depuis le fichier JSON
with open('intents.json', 'r') as json_file:
    data = json.load(json_file)

# Convertir les données pour les stories
stories_data = []

for intent in data['intents']:
    tag = intent['tag']
    patterns = intent['patterns']
    responses = intent['responses']

    # Créer une histoire simple pour chaque intention
    story = {
        "story": f"story_{tag}",
        "steps": []
    }

    # Ajouter les étapes pour chaque intention
    for i in range(len(patterns)):
        story['steps'].append({"intent": tag})
        story['steps'].append({"action": f"utter_{tag}"})

    # Ajouter la réponse en tant qu'action finale
    story['steps'].append({"action": f"utter_{tag}", "responses": responses})

    # Ajouter l'histoire à la liste des stories
    stories_data.append(story)

# Écrire les données dans un fichier YAML pour les stories
with open('stories.yml', 'w') as stories_file:
    yaml.dump(stories_data, stories_file, default_flow_style=False)
