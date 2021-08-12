import requests
from bs4 import BeautifulSoup
from newspaper import Article
from textblob import TextBlob
import nltk

nltk.download('punkt')

feed = "https://abcnews.go.com/abcnews/technologyheadlines"

# first make a get request to the RSS feed
response = requests.get(feed)
# collect the contents of the request
webpage = response.content
# create a BeautifulSoup object that we can then parse to extract the links and title
soup = BeautifulSoup(webpage, features='xml')

# here we find every instance of an <item> tag, collect everything inside each tag, and store them all in a list
items = soup.find_all('item')

# extract the article link within each <item> tag and store in a separate list
articles = []
for item in items:
    link = item.find('link').text
    articles.append(link)

# extract the data from each article, perform sentiment analysis, and then print
for url in articles:
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    # store the necessary data in variables
    title = article.title
    summary = article.summary
    keywords = article.keywords
    text = article.text
    
    # run sentiment analysis on the article text
    # 1) create a Textblob object and then get the sentiment
    text_blob = TextBlob(text)
    sentiment_obj = text_blob.sentiment
    # 2) store the first element in sentiment_obj as polarity and the second element as subjectivity
    polarity = sentiment_obj[0]
    subjectivity = sentiment_obj[1]

    # now we can print out the data
    print('**************************************')
    print(f'Title: {title}')
    print(f'URL: {url}')
    print(f'Keywords: {keywords}')
    print(f'Polarity: {polarity}')
    print(f'Subjectivity: {subjectivity}')
    print(f'Summary: ')
    print(summary)
    print('**************************************')
