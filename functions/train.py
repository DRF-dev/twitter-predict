import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report


def train(dataset: str):
    # Chargement des données de tweets
    df = pd.read_csv(dataset, delimiter=';', converters={'emotion': lambda x: 1 if x == '4' else 0})

    # Séparation des tweets et de leurs étiquettes de sentiment
    input_txt = df['text']
    output = df['emotion']

    # Création d'un objet TfidfVectorizer pour transformer le texte en vecteurs de mots
    vectorizer = TfidfVectorizer()
    input_vec = vectorizer.fit_transform(input_txt.values.astype('str'))

    input_train, input_test, output_train, output_test = train_test_split(input_vec, output, test_size=0.1)

    model = LogisticRegression(max_iter=1_000_000)
    # model = MLPClassifier(hidden_layer_sizes=(32, 32), max_iter=1000)
    # model = SVR()

    model.fit(input_train, output_train)

    predictions = model.predict(input_test)
    accuracy = model.score(input_test, output_test)
    print(f"Précision du modèle: {str('%.2f' % (accuracy * 100))}%")
    print('Confusion matrix test:\n', confusion_matrix(output_test, predictions))
    print('Classification report test:\n', classification_report(output_test, predictions))

    with open('helpers/neural_network.txt', 'wb') as file:
        pickle.dump(model, file)
    with open('helpers/tfid_vectorizer.txt', 'wb') as tfid_file:
        pickle.dump(vectorizer, tfid_file)
