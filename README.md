
# News API Web Application

This project is a simple web application built using **Flask**, a Python web framework. The application fetches news articles from the **News API**, processes the data to extract keywords, and visualizes the most frequent keywords in the articles.

---

### Table of Contents

1. [Project Description](#project-description)
2. [Technologies Used](#technologies-used)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Project Structure](#project-structure)
6. [Features](#features)
7. [Future Enhancements](#future-enhancements)

---

### Project Description

This web application fetches the latest news articles using the **News API** and extracts important keywords from those articles. The extracted keywords are then displayed along with a simple visualization of the most frequent words.

The main goal of this project is to demonstrate the ability to:
- Interact with external APIs
- Process and analyze data
- Visualize data
- Deploy a web application

The project includes:
- A **Flask web application** that serves the news articles.
- **Keyword extraction** from the articles.
- A **data visualization** (bar chart) of the most common keywords in the articles.

---

### Technologies Used

- **Python 3.x**
- **Flask**: A web framework for Python.
- **News API**: Used to fetch real-time news articles.
- **Requests**: Python library to make HTTP requests to the News API.
- **Matplotlib**: Used for visualizing data (in this case, plotting the keyword frequencies).
- **HTML/CSS**: For rendering the frontend.

---

### Installation

#### Prerequisites
To run this project, you need the following:
- Python 3.x installed on your machine.
- A **News API key** (get it from [NewsAPI](https://newsapi.org/)).

#### Steps to Install

1. **Clone the repository** to your local machine:

2. **Create a virtual environment** to manage dependencies (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - For Windows:
     ```bash
     venv\Scriptsctivate
     ```
   - For MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up the API key**:
   - Get your API key from [News API](https://newsapi.org/).
   - Set your API key in the application by creating a `.env` file or modifying the code directly to insert the key:
   ```python
   api_key = 'your_api_key'
   ```

---

### Usage

1. **Run the application**:
   ```bash
   pyth
   python app.py
   ```

2. Open a browser and navigate to `http://127.0.0.1:5000/`.

3. The homepage will display:
   - A list of the latest news articles.
   - A bar chart displaying the most frequent keywords extracted from the articles.

---

### Project Structure

The project has the following structure:

```
news-api-web-app/
├── app.py               # Main Flask application
├── requirements.txt     # List of dependencies
├── news.py              # Python file that handles the News API interaction and keyword extraction
├── templates/
│   ├── index.html       # HTML template for displaying news articles and charts
|
```

- **app.py**: This is the main Python file. It initializes the Flask app, defines routes, fetches news data from the News API, and generates the keyword frequency plot.
- **news.py**: Contains the logic to interact with the News API and process the articles. It fetches the latest news, extracts keywords, and prepares the data for visualization.
- **templates/index.html**: HTML template for the homepage, displaying news articles and keyword frequency chart.

---

### Features

1. **News Fetching**: Retrieves the latest news articles from the News API.
2. **Keyword Extraction**: Processes news articles to extract the most frequently occurring keywords.
3. **Data Visualization**: Plots the frequency of keywords in a bar chart format.
4. **Responsive UI**: The frontend is styled to be user-friendly and visually appealing.

---

### Future Enhancements

1. **Search Functionality**: Allow users to search for news articles based on topics or keywords.
2. **Filter News by Category**: Add categories such as "Sports", "Technology", etc., to display filtered news.
3. **User Authentication**: Add login functionality to store user preferences.
4. **Improved Keyword Extraction**: Use more sophisticated natural language processing (NLP) methods to extract keywords (e.g., using libraries like **spaCy** or **NLTK**).
5. **Deploy the Application**: Deploy the application to a live server like **Heroku**, **AWS**, or **Google Cloud** to make it publicly accessible.

