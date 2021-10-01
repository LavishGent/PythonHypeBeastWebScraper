import time
import display_articles
import the_verge_scraper
import hypebeast_scraper

if __name__ == '__main__':
    while True:
        hypebeast_scraper.find_hypebeast_trending_stories()
        hypebeast_scraper.find_latest_stories()
        the_verge_scraper.find_verge_tech_stories()
        display_articles.display_articles()
        time_wait = 10
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait * 60)