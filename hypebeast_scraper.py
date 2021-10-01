from bs4 import BeautifulSoup
import requests

def find_hypebeast_trending_stories():
    html_text = requests.get('https://hypebeast.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    article_titles = soup.find_all('div', class_ = 'trending-story row no-gutters')
    title_list = []
    link_list = []

    for article_title in article_titles:
        title = article_title.h2.find('a', class_ = 'post-link').text
        link = article_title.a['href']
        title_list.append(title)
        link_list.append(link)
    title_link_pair = dict(zip(title_list, link_list))
    with open(f'text_content/trending_stories.txt', 'w') as f:
        for title, link in title_link_pair.items():
            f.write(f'{title}\n{link}\n\n')


def find_latest_stories():
    html_text = requests.get('https://hypebeast.com/').text
    soup = BeautifulSoup(html_text, 'lxml')
    stories = soup.find_all('div', class_ = 'post-box-content-title')
    title_list = []
    link_list = []

    for story in stories:
        title = story.find('a', class_ = 'title').text
        link = story.a['href']
        title_list.append(title)
        link_list.append(link)
    title_link_pair = dict(zip(title_list, link_list))
    with open(f'text_content/latest_stories.txt', 'w') as f:
        for title, link in title_link_pair.items():
            f.write(f'{title}\n{link}\n\n')
