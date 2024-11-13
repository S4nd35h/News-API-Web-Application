from flask import Flask, render_template, jsonify
from io import BytesIO
import base64
import matplotlib.pyplot as plt
from news import fetch_news, extract_keywords, plot_keywords

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch and process news
    news_list = fetch_news()  # Fetches the news data from an API or source
    news_list = remove_duplicates(news_list)  # Removes duplicate news items
    
    # Extract keywords from descriptions
    keyword_counts = extract_keywords(news_list)
    
    # Generate the keyword frequency plot
    plot_url = None
    if keyword_counts:
        plot_url = plot_keywords(keyword_counts)
    
    # Pass data to the HTML template
    return render_template('index.html', news_data=news_list, plot_url=plot_url)

def remove_duplicates(news_list):
    seen_titles = set()
    unique_news = []
    for article in news_list:
        title = article.get('title')
        if title and title not in seen_titles:
            unique_news.append(article)
            seen_titles.add(title)
    return unique_news

if __name__ == '__main__':
    app.run(debug=True)
