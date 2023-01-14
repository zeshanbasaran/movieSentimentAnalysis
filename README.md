# movieSentimentAnalysis

## Introduction

This python script uses natural language processing (NLP) and machine learning algorithms from scikit-learn to analyze a user's sentiment regarding a movie. The dataset is a collection of IMDB reviews from Kaggle.

It works by taking 1000 positive and 1000 negative movies review from the dataset to train and test

![image](https://user-images.githubusercontent.com/116126778/212489675-2d5bf155-c9cb-41b0-8e02-17bba8541ecf.png)

and begins to associate certain words with a positive or negative sentinment .

### Example:

Positive sentinment words = "good", "great", "amazing", "best", "love"...

![image](https://user-images.githubusercontent.com/116126778/212490773-6c3023d6-885d-45ae-8735-b74325824e26.png)

Negative sentinment words = "bad", "terrible", "hate", "awful", "trash"...

![image](https://user-images.githubusercontent.com/116126778/212490801-44c1a0d9-2f1d-4fd6-9bef-06ef7a047dbd.png)

Using the predict function from scikit-learn, the script is able to determine if a user-entered movie review is positive or negative, and return a response to match.

![image](https://user-images.githubusercontent.com/116126778/212491760-49949df1-64a0-48f6-bf9a-8e09c36ad06a.png)

## Limitations

The dataset only had positive and negative reviews to train from, so the script is unable to recognize neutral sentinment. Interestingly, "okay" was assocaited with positive sentiment

![image](https://user-images.githubusercontent.com/116126778/212490071-64e3dff5-bf14-4f5a-b857-c0176e1d0f65.png)

while "ok" was associated with negative sentiment.

![image](https://user-images.githubusercontent.com/116126778/212490124-ae757aa8-3e7e-48c9-8ef3-a817bb27c0d6.png)

It also struggled to understand some slang that may have not been present in the dataset. Cuss words were very hit-or-miss, since the same one can have a different meaning depending on the context. 

![image](https://user-images.githubusercontent.com/116126778/212490614-1fd57997-57e4-4236-aa89-d875f69da2eb.png)

## Credits

### Research Materials:
- [A Simple Guide to Scikit-Learn](https://towardsdatascience.com/a-beginners-guide-to-text-classification-with-scikit-learn-632357e16f3a) by The PyCoach

### Datasets:
- [IMDB Dataset of 50K Movie Reviews](https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews?resource=download) by Lakshmipathi N
