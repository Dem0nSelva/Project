import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')


def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z\s]', '', text)  # Remove non-alphabet characters
    text = text.lower()  # Convert to lowercase
    text = word_tokenize(text)  # Tokenize
    text = [word for word in text if word not in stopwords.words('english')]  # Remove stopwords
    return ' '.join(text)


def analyze_sentiment(texts):
    sia = SentimentIntensityAnalyzer()
    results = {'pos': 0, 'neu': 0, 'neg': 0}
    for text in texts:
        sentiment = sia.polarity_scores(text)
        if sentiment['compound'] >= 0.05:
            results['pos'] += 1
        elif sentiment['compound'] <= -0.05:
            results['neg'] += 1
        else:
            results['neu'] += 1

    total = len(texts)
    for key in results:
        results[key] = results[key] / total

    return results
