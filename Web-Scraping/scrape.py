#!/usr/bin/python3
'''Python file for scrapping data from a website
   specifically - (Hackers News site) 
   Scrape news(title, link and votes) data of the site having upto 100 votes
   ordered with the number of votes(highest to lowest)
'''
import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news') #request data with site link
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline')
subtext = soup.select('.subtext')


def sort_stories_by_votes(news_list):
    '''function to sort the news'''
    return sorted(news_list, key = lambda k:k['votes'], reverse=True)


def create_custom_news(links, subtext):
    '''function that create list of the news
       having up to hundred votes
    '''
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
