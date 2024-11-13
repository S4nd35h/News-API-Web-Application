import requests
from collections import Counter
import matplotlib.pyplot as plt
from io import BytesIO
import base64

def fetch_news():
    # Replace with your actual news API URL or source
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=#ADD_YOUR_API_KEY_HERE" 
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        return []

def extract_keywords(news_list):
    all_keywords = []
    for article in news_list:
        description = article.get('description', '')
        if description:
            all_keywords.extend(description.lower().split())  # Lowercase and basic split for simplicity
    keyword_counts = Counter(all_keywords)
    return keyword_counts

def plot_keywords(keyword_counts):
    # Get the top 10 most common keywords
    top_keywords = keyword_counts.most_common(10)
    if not top_keywords:
        return None
    
    # Separate keywords and their counts for plotting
    keywords, counts = zip(*top_keywords)
    
    # Plot the keywords and their frequencies
    plt.figure(figsize=(10, 6))
    plt.bar(keywords, counts, color='skyblue')
    plt.title("Top 10 Keywords in News Articles")
    plt.xlabel("Keywords")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot to a BytesIO object and encode as base64 for HTML rendering
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    plt.close()
    
    return f"data:image/png;base64,{plot_url}"
