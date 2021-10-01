from bs4 import BeautifulSoup
import requests

def find_hypebeast_trending_stories():
    html_text = requests.get('https://hypebeast.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    article_titles = soup.find_all('div', class_ = 'trending-story row no-gutters')

    for article_title in article_titles:
        title = article_title.find('a', class_ = 'post-link').text
        link = article_title.a['href']
        print(title + '\n' + link + '\n')
def find_latest_stories():
    html_text = requests.get('https://hypebeast.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    stories = soup.find_all('div', class_ = 'post-box-content-title')

    for story in stories:
        title = story.find('a', class_ = 'title').text
        link = story.a['href']
        print(title + '\n' + link + '\n')

find_latest_stories()
find_hypebeast_trending_stories()