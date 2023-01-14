# File:     movieSentinementAnalysis
# Author:   Zeshan Basaran

import pandas as pd

df_review = pd.read_csv('IMDBDataset.csv')

# Small sample - 1000 positive and 1000 negative reviews
df_positive = df_review[df_review['sentiment']=='positive'][:1000]
df_negative = df_review[df_review['sentiment']=='negative'][:1000]
df_review_imb = pd.concat([df_positive, df_negative])   # Dataset

from sklearn.model_selection import train_test_split
train, test = train_test_split(df_review_imb, test_size=0.33, random_state=42)

# Training = 33%, Testing = 67%
train_x, train_y = train['review'], train['sentiment']
test_x, test_y = test['review'], test['sentiment']

# Identifies words that relate to sentiment
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
train_x_vector = tfidf.fit_transform(train_x)
train_x_vector

test_x_vector = tfidf.transform(test_x)

# Input = reviews, Output = sentiment
from sklearn.svm import SVC
svc = SVC(kernel='linear')
svc.fit(train_x_vector, train_y)

# Test predictions
print("Calibrating...")
print(svc.predict(tfidf.transform(['A good movie'])))
print(svc.predict(tfidf.transform(['An excellent movie'])))
print(svc.predict(tfidf.transform(['I did not like this movie at all'])))

# Predict user sentinment regarding movie
print("\nI want to ask you about movies. Type 'q' to quit at any time.")
phrase = input("\nWhat did you think about the movie? ")

while phrase != "q":
    verdict = (svc.predict(tfidf.transform([phrase])))

    if verdict == 'positive':
        print("I can tell you liked it!")
    else:
        print("Oh no, I can tell you didn't like it :(")

    phrase = input("\nWhat did you think about the movie? ")

print("\nThanks for the feedback!")

