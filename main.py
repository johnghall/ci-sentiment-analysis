# import nltk
import sys, getopt
from nltk.sentiment import SentimentIntensityAnalyzer
from random import shuffle
sia = SentimentIntensityAnalyzer()


def get_sentiment(response: str) -> bool:
    """True if tweet has positive compound sentiment, False otherwise."""
    score = sia.polarity_scores(response)["compound"]
    if score <= -.2:
        return "Negative"
    elif score < .2:
        return "Neutral"
    else:
        return "Positive"

def print_sorted_list():
    sorted_sentiments = {"Negative": [], "Neutral": [], "Positive": []}

    for response in sample_responses:
        sorted_sentiments[get_sentiment(response)].append(response)

    print("Negative: \n")
    for response in sorted_sentiments["Negative"]:
        print(response)

    print("\n \n")

    print("Neutral: \n")
    for response in sorted_sentiments["Neutral"]:
        print(response)

    print("\n \n")

    print("Positive: \n")
    for response in sorted_sentiments["Positive"]:
        print(response)