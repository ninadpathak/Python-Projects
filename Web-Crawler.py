import requests
from bs4 import BeautifulSoup
import urllib
import time

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"


def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # This div contains the article's body
    # (June 2017 Note: Body nested in two div tags)
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")
    article_link = None

    for element in content_div.find_all("p", recursive=False):
        if element.find("a", recursive=False):
            article_link = element.find("a", recursive=False).get("href")
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link


def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print(search_history[-1])
        print("Target URL reached! Yey!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print(search_history[-1])
        print("Hey, we already saw this URL! Dont want to get stuck in the infinite loop")
        return False
    elif len(search_history) > max_steps:
        print(search_history[-1])
        print("Isn't this taking too much time already?")
        return False
    else:
        return True


article_chain = [start_url]


while continue_crawl(article_chain, target_url, 500):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(1)