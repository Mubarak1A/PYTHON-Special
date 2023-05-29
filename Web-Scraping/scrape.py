import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')



def sort_stories_by_votes(news_list):
    return sorted(news_list, key = lambda k:k['votes'], reverse=True)


def create_custom_news(links, subtext):
    news = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find('a').get('href')
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                news.append({'title': title, 'link': href, 'votes': points})
        
    return sort_stories_by_votes(news)


pprint.pprint(create_custom_news(links, subtext)) 
