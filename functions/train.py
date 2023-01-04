import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neural_network import MLPClassifier


def train(dataset: str):
    # Chargement des données de tweets
    df = pd.read_csv(dataset, delimiter=';')

    # Séparation des tweets et de leurs étiquettes de sentiment
    input_txt = df['text']
    output = df['emotion']

    # Création d'un objet TfidfVectorizer pour transformer le texte en vecteurs de mots
    vectorizer = TfidfVectorizer()
    input_vec = vectorizer.fit_transform(input_txt.values.astype('str'))

    # Séparation des données en ensemble d'entraînement et de test
    input_train, input_test, output_train, output_test = train_test_split(input_vec, output, test_size=0.1)

    # Création d'un modèle de régression logistique
    model = LogisticRegression(max_iter=1_000_000)
    # model = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=1000)

    # Entraînement du modèle sur les données d'entraînement
    model.fit(input_train, output_train)

    # Évaluation du modèle sur les données de test
    predictions = model.predict(input_test)
    accuracy = model.score(input_test, output_test)
    print(f"Précision du modèle: {str('%.2f' % (accuracy * 100))}%")
    print('Confusion matrix test:\n', confusion_matrix(output_test, predictions))
    print('\nClassification report test:\n', classification_report(output_test, predictions))

    # Prédiction du sentiment de nouveaux tweets
    new_tweets_arr = ['This product is amazing!', 'I hate this company']
    new_tweets_vec = vectorizer.transform(new_tweets_arr)

    predictions = model.predict(new_tweets_vec)
    print('Prédictions:', new_tweets_arr, predictions)
