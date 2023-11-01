# Import neccessary libraries and modules
from flask import Flask, render_template, request
from newsapi.newsapi_client import NewsApiClient
from config import API_KEY

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import string
import base64
from io import BytesIO

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, FreqDist

# Initialize a Flask web application
app = Flask(__name__)

# Define the route for the main page
@app.route('/')
def index():
    return render_template('index.html')    # Renders the 'index.html' template

# Define the route for processing user input and displaying results
@app.route('/query_articles', methods=['POST'])
def query_articles():
    user_topic = request.form['user_topic'] # Get the user's topic of interest from the form

    # Create an instance of the News API client
    newsapi = NewsApiClient(api_key=API_KEY)

    # Call the News API to fecth news articles based on the user's topic
    all_articles = newsapi.get_everything(q=user_topic, language='en', sort_by='relevancy')
    df = pd.DataFrame(all_articles['articles'])

    # Perform sentiment ananlysis on the content of the articles
    df['content'] = df['content'].apply(preprocess_text)
    df['content_sentiment'] = df['content'].apply(get_sentiment)

    # Filter news articles by sentiment
    positive_df = df[df['content_sentiment'] == 'positive']
    negative_df = df[df['content_sentiment'] == 'negative']
    neutral_df = df[df['content_sentiment'] == 'neutral']

    # Create word clouds for each sentiment category
    wordcloud_positive = create_wordcloud(positive_df, 'Positive Sentiment')
    wordcloud_negative = create_wordcloud(negative_df, 'Negative Sentiment')
    wordcloud_neutral = create_wordcloud(neutral_df, 'Neutral Sentiment')

    # Calculate the distribution of sentiments in the data
    sentiment_counts = df['content_sentiment'].value_counts()
    sentiments = sentiment_counts.index
    count = sentiment_counts.values

    return render_template('result.html', user_topic=user_topic, sentiments=sentiments, count=count, 
                           wordcloud_positive=wordcloud_positive, wordcloud_negative=wordcloud_negative, 
                           wordcloud_neutral=wordcloud_neutral)

# Preprocess text data for sentiment analysis
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove HTML tags
    pattern = r'<[^>]+>'
    text = re.sub(pattern, '', text)
    # Remove URLs
    pattern = r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    text = re.sub(pattern, '', text)
    # Remove punctuation and special characters
    text = ''.join([char for char in text if char not in string.punctuation])
    # Remove the word 'chars'
    text = text.replace('chars', '')
    # Remove text like 'via Getty Images'
    text = re.sub(r'\b(via|getty|images)\b', '', text)
    # Tokenize the text
    tokens = word_tokenize(text)
    fdist = FreqDist(tokens)
    # Filter out low-frequency words
    filtered_words = [token for token in tokens if fdist[token] < fdist.N() * 0.1]
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in filtered_words if word not in stop_words]
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

# Perform sentiment anañysis using VADER SentimentIntensityAnalyzer
def get_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)
    compound_score = sentiment['compound']
    if compound_score >= 0.5:
        return 'positive'
    elif compound_score <= -0.5:
        return 'negative'
    else:
        return 'neutral'

# Generate a word cloud and return it as a base64-encoded image
def create_wordcloud(dataframe, title):
    all_text = ' '.join(dataframe['content'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)
    
    # Generate the image as a BytesIO object
    img_buffer = BytesIO()
    wordcloud.to_image().save(img_buffer, format="PNG")
    
    # Convert the bytes buffer to bytes
    img_bytes = img_buffer.getvalue()

    # Convert the image to base64 format
    image_base64 = base64.b64encode(img_bytes).decode('utf8')
    
    return image_base64

# Start the Flask application when executed directly
if __name__ == '__main__':
    app.run(debug=True)