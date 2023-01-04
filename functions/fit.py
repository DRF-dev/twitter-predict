import os
import pickle

from sklearn.feature_extraction.text import CountVectorizer


def fit():
    if os.path.exists('neural_network.txt'):
        with open('neural_network.txt', 'rb') as file:
            model = pickle.load(file)
    else:
        raise Exception('neural_network does not actually exist')

    new_tweets_arr = ['This product is amazing!', 'I hate this company']
    new_tweets = CountVectorizer().transform(new_tweets_arr)
    predictions = model.predict(new_tweets)
    print('Prédictions:', new_tweets, predictions)
