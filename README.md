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

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/alexquilis1/sentiment_analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd sentiment_analysis
   ```
3. Installad the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your News API key to the 'config.py' file.

## Usage
1. Run the application:
   ```
    python app.py
   ```
3. Open a web browser and go to http://localhost:5000/ to access the app.
4. Enter a topic of interest, and the app will retrieve news articles and perform sentiment analysis.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
