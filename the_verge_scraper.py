from bs4 import BeautifulSoup
import requests


def find_verge_tech_stories():
    html_text = requests.get('https://www.theverge.com/ai-artificial-intelligence').text
    soup = BeautifulSoup(html_text, 'lxml')
    article_titles = soup.find_all('div', class_='c-entry-box--compact__body')
    title_list = []
    link_list = []

    for article_title in article_titles:
        title = article_title.h2.find('a').text
        link = article_title.a['href']
        title_list.append(title)
        link_list.append(link)
    title_link_pair = dict(zip(title_list, link_list))
    with open(f'text_content/the_verge_tech.txt', 'w') as f:
        for title, link in title_link_pair.items():
            f.write(f'{title}\n{link}\n\n')
