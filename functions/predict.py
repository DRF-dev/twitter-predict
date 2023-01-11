import os
import pickle
from typing import List

class Tweet:
    def __init__(self, text: str, positif: float, negative: float):
        self.text = text
        self.positif = positif
        self.negative = negative

    def to_json(self):
        return {
            "text": self.text,
            "positif": str('%.2f' % (self.positif * 100)) + "%",
            "negative": str('%.2f' % (self.negative * 100)) + "%"
        }

def predict(texts: List[str]):
    if os.path.exists('helpers/neural_network.txt'):
        with open('helpers/neural_network.txt', 'rb') as file:
            model = pickle.load(file)
    else:
        raise Exception('neural_network does not actually exist')

    if os.path.exists('helpers/tfid_vectorizer.txt'):
        with open('helpers/tfid_vectorizer.txt', 'rb') as file:
            vectorizer = pickle.load(file)
    else:
        raise Exception('neural_network does not actually exist')

    new_tweets_vec = vectorizer.transform(texts)

    predictions = model.predict_proba(new_tweets_vec)

    list_of_tweets: List[Tweet] = []
    for i in range(len(texts)):
        tweet_stats = Tweet(text=texts[i], positif=predictions[i][1], negative=predictions[i][0])
        list_of_tweets.append(tweet_stats)

    return list(map(lambda x: x.to_json(), list_of_tweets))
