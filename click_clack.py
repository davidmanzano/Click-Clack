from __future__ import division
import requests
from bs4 import BeautifulSoup
import re
import random
import time
import urllib.request as u

scraping_url = 'https://www.philosophybasics.com/general_quotes.html'
api_url = 'http://quotesondesign.com/wp-json/posts?filter[orderby]=rand&filter[posts_per_page]=1&callback='

def calcWPM(typed_entries, elapsed_time):
    return (typed_entries / 5.0) / (elapsed_time / 60.0)

def play(quote):
    typed_entries = len(quote[0])
    print(typed_entries)
    time.sleep(1)
    start_time = time.time()
    user_text = input(quote[0] + "\n")

    if(user_text != quote[0]):
        print("Incorrect!\n")        
    else:
        elapsed_time = time.time() - start_time
        print("Correct!\n")
        wpm = calcWPM(typed_entries, elapsed_time)
        print(str(wpm) + "\n")


while(True):    
    if(random.choice([0,1])):
        response = requests.get(scraping_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        num = random.randint(0, 72)
        row = soup.select('li:nth-of-type(%d)' % num)
        m = re.findall('<li>“(.+?)” – ', str(row))
    else:
        response = requests.get(api_url)
        m = re.findall('<p>(.+?).<', str(response.content))
    
    play(m)
    

