# 📊 News Sentiment Analysis Web App

> A Flask-powered web application that analyzes sentiment in news articles and generates beautiful word clouds to visualize emotional trends in current events.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 What it does

This web app takes any topic you're curious about and:
- 🔍 Fetches the latest news articles from across the web
- 🧠 Analyzes the emotional tone of each article
- 📈 Shows you whether the coverage is positive, negative, or neutral
- ☁️ Creates stunning word clouds to visualize the most common terms

Perfect for understanding public sentiment on current events, trending topics, or any subject you're researching!

## ✨ Features

- **🔎 Smart Topic Search** - Enter any keyword and get relevant news articles
- **😊😐😞 Sentiment Classification** - Automatic categorization into positive, negative, and neutral
- **📊 Visual Analytics** - Beautiful charts showing sentiment distribution  
- **☁️ Word Cloud Generation** - Separate word clouds for each sentiment category
- **🧹 Intelligent Text Processing** - Removes noise, URLs, and irrelevant content
- **🌐 Real-time Data** - Fresh news articles from the News API

## 🛠️ Built With

- **[Flask](https://flask.palletsprojects.com/)** - Lightweight Python web framework
- **[News API](https://newsapi.org/)** - Real-time news data source
- **[NLTK](https://www.nltk.org/)** - Natural language processing toolkit
- **[VADER Sentiment](https://github.com/cjhutto/vaderSentiment)** - Lexicon-based sentiment analysis
- **[WordCloud](https://github.com/amueller/word_cloud)** - Word cloud generation
- **[Pandas](https://pandas.pydata.org/)** - Data manipulation and analysis

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- A [News API key](https://newsapi.org/register) (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/alexquilis1/news-sentiment-analyzer.git
   cd sentiment_analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `config.py` file in the project root:
   ```python
   API_KEY = "your_news_api_key_here"
   ```

4. **Download NLTK data** (first time only)
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```

### Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Enter a topic** (e.g., "climate change", "artificial intelligence", "olympics")

4. **Explore the results** - View sentiment distribution and word clouds!

## 🎓 What I Learned

This was one of my early Python projects where I explored:
- Web development with Flask
- Natural language processing techniques
- Data visualization and web scraping
- API integration and data manipulation
- Text preprocessing and sentiment analysis algorithms

## 🤝 Contributing

Feel free to dive in! [Open an issue](https://github.com/alexquilis1/news-sentiment-analyzer/issues) or submit a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Alex Quilis** - [alexquilis1](https://github.com/alexquilis1)

---

⭐ **Enjoyed this project?** Give it a star to show your support!
