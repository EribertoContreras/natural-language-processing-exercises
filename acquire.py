from requests import get
from bs4 import BeautifulSoup
import os
import pandas as pd

"""
Codeup Blog Articles

- Visit Codeup's Blog and record the urls for at least 5 distinct blog posts. For each post, you should scrape at least the post's title and content.

- Encapsulate your work in a function named get_blog_articles that will return a list of dictionaries, with each dictionary representing one article. The shape of each dictionary should look like this:


`{
    'title': 'the title of the article',
    'content': 'the full text content of the article'
}`

- Plus any additional properties you think might be helpful.
"""
def blog_articles():
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent

    response = get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    links = [a['href'] for a in soup.select('h2 a[href]')]

    articles = []

    for url in links:
        url_response = get(url, headers=headers)
        soup = BeautifulSoup(url_response.text)
        
        title = soup.find('h1', class_='entry-title'). text
        content = soup.find('div', class_='entry-content').text.strip()
        
        article_dict = {
            'title': title,
            'content': content,
        }
        
        articles.append(article_dict)
        # use code like (articles[0:5]) to summon articles
    return pd.DataFrame(articles)


""" make into data frame using import pandas as pd
pd.DataFrame(articles) """
""" for individual === use this type of code"""

def in_person_workshop_data():
    url = "https://codeup.com/workshops/in-person-workshop-learn-to-code-python-on-7-19/"
    headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
    response = get(url, headers=headers)
    # Make a soup variable holding the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', class_='entry-title'). text
    content = soup.find('div', class_='entry-content').text.strip()
    article = []
    article_dict = {
        'title': title,
        'content': content,
    }

    article.append(article_dict)
    return article

def free_javascript_data():
    url = "https://codeup.com/workshops/dallas/free-javascript-workshop-at-codeup-dallas-on-6-28/"
    headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
    response = get(url, headers=headers)
    response.text
    # Make a soup variable holding the response content
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', class_='entry-title'). text
    content = soup.find('div', class_='entry-content').text.strip()
    article = []
    article_dict = {
        'title': title,
        'content': content,
    }

    article.append(article_dict)
    return article
def tips_for_prospective_students():
        url = "https://codeup.com/tips-for-prospective-students/is-our-cloud-administration-program-right-for-you/"
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        response.text
        # Make a soup variable holding the response content
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='entry-title'). text
        content = soup.find('div', class_='entry-content').text.strip()
        article = []
        article_dict = {
            'title': title,
            'content': content,
        }

        article.append(article_dict)
        return article
def pride_in_tech_panel():
        url = "https://codeup.com/workshops/pride-in-tech-panel/"
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        response.text
        # Make a soup variable holding the response content
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='entry-title'). text
        content = soup.find('div', class_='entry-content').text.strip()
        article = []
        article_dict = {
            'title': title,
            'content': content,
        }

        article.append(article_dict)
        return article
def tips_for_prospective_students():
        url = "https://codeup.com/tips-for-prospective-students/mental-health-first-aid-training/"
        headers = {'User-Agent': 'Codeup Data Science'} # Some websites don't accept the pyhon-requests default user-agent
        response = get(url, headers=headers)
        response.text
        # Make a soup variable holding the response content
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='entry-title'). text
        content = soup.find('div', class_='entry-content').text.strip()
        article = []
        article_dict = {
            'title': title,
            'content': content,
        }

        article.append(article_dict)
        return article

""" 
News Articles

- We will now be scraping text data from inshorts, a website that provides a brief overview of many different topics.

- Write a function that scrapes the news articles for the following topics:

    - Business
    - Sports
    - Technology
    - Entertainment
The end product of this should be a function named get_news_articles that returns a list of dictionaries, where each dictionary has this shape:


`{
    'title': 'The article title',
    'content': 'The article content',
    'category': 'business' # for example
}`
"""

def get_shorts_articles(categories, refresh = False):
        
    #Creating an empty list to contain DataFrames of scraped data components:
    inshorts_articles = []
   #for-loop to pull categories:
    for category in categories:
        #Creating an empty dataframe:
        is_articles = pd.DataFrame()
        #making url:
        url = f'https://inshorts.com/en/read/{category}'
        #making header so it doesn't use'python-request':
        headers = {'User-Agent': 'Codeup Data Science'}
        #response from the website:
        response = get(url, headers=headers)
        #Creating a beautifulSoup:
        soup = BeautifulSoup(response.content, 'html.parser') 
        # creating a list for titles:
        titles = soup.find_all(itemprop = 'headline')
        #Creating a list of all article bodies in the given category
        contents = soup.find_all(itemprop = 'articleBody')
        #Adding 'title' column to DataFrame containing title text for each article:
        is_articles['title'] = [title.text for title in titles]
        #Adding 'contents' column to DataFrame containing article body text for each article
        is_articles['contents'] = [content.text for content in contents]
        #Adding 'category' column to list category for each article in the category:
        is_articles['category'] = category
        #Appending DataFrame for each category to overall list of DataFrames:
        inshorts_articles.append(is_articles)

    #Concatenating all of the DataFrames in the list to create one large DataFrame:
    inshorts = pd.concat(inshorts_articles)
    #Returning final DataFrame:
    return inshorts
""" use this to summon code properly"""
#categories chosen
# categories = ['world', 'science', 'technology', 'entertainment']
# inshorts = get_shorts_articles(categories)
# inshorts