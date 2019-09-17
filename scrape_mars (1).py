
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import time
from selenium import webdriver

executable_path ={'executable_path':'C:/Users/BADOU/chromedriver_win32 (6)/chromedriver.exe'}
browser=Browser('chrome', **executable_path, headless=False)
url1 = 'https://mars.nasa.gov/news/'
# Retrieve page with the requests module
browser.visit(url1)
html=browser.html
soup1 = bs(html, "html5lib")
print(soup1.prettify)
news_title = soup1.find_all('div', class_='content_title')[0].find('a').text.strip()

#print title 
print(news_title)
# Extract the paragraph from the class="rollover_description_inner" and clean up the text use strip
news_p = soup1.find_all('div',class_='rollover_description_inner')[0].text.strip()
print(news_p)
# Execute Chromedriver
executable_path ={'executable_path':'C:/Users/BADOU/chromedriver_win32 (6)/chromedriver.exe'}
browser=Browser('chrome', **executable_path, headless=False)
# URL of page to be scraped
url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

# the browser to visit the page
browser.visit(url2)
# assign the page conetnt  to html
html = browser.html
# Create a Beautiful Soup object
soup2 = bs(html, "html5lib")
print(soup2.prettify)
#Scrape Path for the Feature Image. got the partial path of the url
partial_address=soup2.find_all('a' ,class_='fancybox')[0].get('data-fancybox-href').strip()
#combine the url to get the full address
featured_image_url = "https://www.jpl.nasa.gov"+partial_address
#Print to check the full URL
print(featured_image_url)
#browse to check url
browser.visit(featured_image_url)
#NASA MARS weather
# Execute Chromedriver
executable_path ={'executable_path':'C:/Users/BADOU/chromedriver_win32 (6)/chromedriver.exe'}
browser=Browser('chrome', **executable_path, headless=False)
# URL of page to be scraped
url3 = 'https://twitter.com/marswxreport?lang=en'
#Visit the page using the browser
browser.visit(url3)
# assign html content
html = browser.html
# Create a Beautiful Soup object
soup3 = bs(html, "html5lib")
print(soup3.prettify)
#scrap latest Mars weather tweet
mars_weather = soup3.find_all('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text')[0].text
print(mars_weather)
# Execute Chromedriver
executable_path ={'executable_path':'C:/Users/BADOU/chromedriver_win32 (6)/chromedriver.exe'}
browser=Browser('chrome', **executable_path, headless=False)
# URL of page to be scraped
url4 = 'https://space-facts.com/mars/'
#visit the page using the browser
browser.visit
html = browser.html
# Create a Beautiful Soup object
soup4 = bs(html, "html5lib")
print(soup4.prettify)
# use Pandas to get the url table
tables = pd.read_html(url4)
tables
# Convert list of table into pandas dataframe
df = tables[0]

# update column name
df.columns=['description','Mars_Value','Earth_Mars']

# inspect dataframe
df
#let set the description as the index

df.set_index('description', inplace=True)
df
df.to_html('table.html')
# Execute Chromedriver
executable_path ={'executable_path':'C:/Users/BADOU/chromedriver_win32 (6)/chromedriver.exe'}
browser=Browser('chrome', **executable_path, headless=False)
# URL of page to be scraped
url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

#Visit the page using the browser
browser.visit(url5)
# assign the page content the html 
html = browser.html
# Create a Beautiful Soup object
soup5 = bs(html,"html5lib")
print(soup5.prettify)
# assigned list to store:
hemisphere_image_urls = []
# create empty dict
dict = {}
# get all the title
results=soup5.find_all('a',class_='icon')[0].text.strip()
# Loop through each result
for result in results:
    item = result.text
    time.sleep(1)    
    browser.click_link_by_partial_text(item)
    time.sleep(1)
    html = browser.html
    soup = bs(html,"html5lib")
    time.sleep(1)
    link = soupa.find_all('div', class_="downloads")[0].find_all('a')[0].get("href")
    time.sleep(1)
    dict["title"]=item
    dict["img_url"]=link 
    hemisphere_image_urls.append(dict)
    dict = {}
    browser.click_link_by_partial_text(item)
    time.sleep(1)
hemisphere_image_urls




