# Twitter-prediction
Cette API est développée en utilisant le framework FastAPI. Il s'agit d'une API RESTful qui vous permet de prédire si un texte est connoté positif ou négatif.

## Prérequis
Avant de démarrer, vous aurez besoin de :
- Python 3.6 ou supérieur
- Un environnement virtuel (facultatif, mais fortement recommandé)

## Installation
1. Clonez ce dépôt sur votre ordinateur local
```bash
git clone https://github.com/DRF-dev/twitter-predict.git
```
2. Accédez au répertoire de l'application
```bash
cd twitter-predict
```

## Utilisation
1. Démarrez le serveur de développement
```bash
uvicorn main:app --reload
```
2. Faites des requêtes sur l'API en utilisant un outil tel que Postman ou Insomnia

## Routes
Les routes disponibles sur l'API sont les suivantes :
- POST /train
  - Créer un réseau de neurone à partir du dataset présent
- POST /predict
  - Prédit l'émotion d'un tweet
  - Exemple de body:
    - ```json
      {
        "texts": ["tweet1", "tweet2"]
      }
      ```

## Contribuer
Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre une pull request.

## Licence
Ce projet n'est pas sous licence.