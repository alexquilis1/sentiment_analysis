# Sentiment Analysis Web App

This is a simple web application for performing sentiment analysis on news articles. Users can enter a topic of interest, and the app fetches related news articles, analyzes their sentiment, and displays the results including word clouds for different sentiments.

## Features

- **User Input**: Users can enter a topic of interest.
- **Data Retrieval**: The app fetches news articles related to the user's topic using the News API.
- **Sentiment Analysis**: Sentiment analysis is performed on the content of the articles.
- **Visualization**: The app displays the distribution of sentiments and word clouds for positive, negative, and neutral sentiments.
- **Preprocessing**: Text data is preprocessed to remove HTML tags, URLs, punctuation, and stopwords.

## Technologies Used

- Flask: A Python web framework for building web applications.
- News API: Used for fetching news articles.
- NLTK (Natural Language Toolkit): For text preprocessing and sentiment analysis.
- VADER SentimentIntensityAnalyzer: Used to perform sentiment analysis.
- WordCloud: To generate word clouds.
