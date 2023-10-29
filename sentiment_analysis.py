from newsapi.newsapi_client import NewsApiClient
from config import API_KEY

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize, FreqDist

def preprocess_text(text):
    # Convertir a minúsculas
    text = text.lower()
    # Eliminar código HTML
    pattern = r'<[^>]+>'
    text = re.sub(pattern, '', text)
    # Eliminar URL
    pattern = r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    text = re.sub(pattern, '', text)
    # Eliminar puntuación y caracteres especiales
    text = ''.join([char for char in text if char not in string.punctuation])
    # Eliminar la palabra "chars"
    text = text.replace('chars', '')
    # Eliminar texto "via Getty Images"
    text = re.sub(r'\b(via|getty|images)\b', '', text)
    # Tokenización
    tokens = word_tokenize(text)
    fdist = FreqDist(tokens)
    filtered_words = [token for token in tokens if fdist[token] < fdist.N() * 0.1]
    # Eliminar palabras vacías
    stop_words = set(stopwords.words('english'))
    words = [word for word in filtered_words if word not in stop_words]
    # Lematización
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

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

def create_wordcloud(dataframe, title, subplot):
    all_text = ' '.join(dataframe['content'])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

    subplot.imshow(wordcloud, interpolation='bilinear')
    subplot.axis('off')
    subplot.set_title(title)

def main(user_topic):
    # Crear una instancia de la API de News
    newsapi = NewsApiClient(api_key=API_KEY)

    # Llamar a la API de News y procesar los datos
    all_articles = newsapi.get_everything(q=user_topic, language='en', sort_by='relevancy')
    df = pd.DataFrame(all_articles['articles'])

    # Realizar el análisis de sentimiento
    analyzer = SentimentIntensityAnalyzer()
    df['content'] = df['content'].apply(preprocess_text)
    df['content_sentiment'] = df['content'].apply(get_sentiment)

    # Filtrar noticias por sentimiento
    positive_df = df[df['content_sentiment'] == 'positive']
    negative_df = df[df['content_sentiment'] == 'negative']
    neutral_df = df[df['content_sentiment'] == 'neutral']

    # Crear gráficos y visualizaciones
    fig, axs = plt.subplots(1, 3, figsize=(20, 20))
    plt.subplots_adjust(wspace=0.2)
    create_wordcloud(positive_df, 'Positive Sentiment', axs[0])
    create_wordcloud(negative_df, 'Negative Sentiment', axs[1])
    create_wordcloud(neutral_df, 'Neutral Sentiment', axs[2])

    plt.show()

    # Crear un gráfico de barras para mostrar la distribución de sentimientos
    sentiment_counts = df['content_sentiment'].value_counts()
    sentiments = sentiment_counts.index
    count = sentiment_counts.values

    plt.bar(sentiments, count)
    plt.xlabel('Sentimiento')
    plt.ylabel('Conteo')
    plt.title('Distribución de Sentimiento en las Noticias (Contenido)')
    plt.show()

if __name__ == '__main__':
    user_topic = input('Por favor, ingresa un tema:')
    main(user_topic)