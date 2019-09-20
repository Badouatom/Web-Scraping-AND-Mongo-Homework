
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
import time
from selenium import webdriver


# In[46]:

# Execute Chromedriver
executable_path ={'executable_path':'C:/Users/BADOU/chromedriver_win32 (6)/chromedriver.exe'}
browser=Browser('chrome', **executable_path, headless=False)

# URL of page to be scraped
url1 = 'https://mars.nasa.gov/news/'
# Retrieve page with the requests module
browser.visit(url1)
html=browser.html
soup1 = bs(html, "html5lib")
print(soup1.prettify)
# Extract the text from the class="content_title" and  use strip to display
news_title = soup1.find_all('div', class_='content_title')[0].find('a').text.strip()

#print title 
print(news_title)

# Extract the paragraph from the class="rollover_description_inner" and clean up the text use strip
news_p = soup1.find_all('div',class_='rollover_description_inner')[0].text.strip()
#print paragraph to check
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
# assign html content
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
# svae the table as html file
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
# assigned list to store:
hemisphere_image_urls = []
url='https://astrogeology.usgs.gov/search/map/Mars/viking/cerberus_enhanced'
response=requests.get(url)
soup=bs(response.text,'html.parser')
cerberus_image=soup.find_all('div',class_='wide-image-wrapper')
cerberus_image
for image in cerberus_image:
        cerberus_picture =image.find('li')
        full_picture = cerberus_picture.find('a')['href']
                      
cerberus_title = soup.find('h2', class_='title').text()

cerberus_hemisphere = {"Title":cerberus_title,   "url":full_picture}

print(cerberus_hemisphere)
hemisphere_image_urls.append(cerberus_hemisphere)
url='https://astrogeology.usgs.gov/search/map/Mars/viking/schiaparelli_enhanced'
response=requests.get(url)
soup=bs(response.text,'html.parser')
print(soup.prettify)


schiaparelli_image=soup.find_all('div',class_='wide-image-wrapper')
for image in schiaparelli_image:
            schiaparelli_picture=image.find('li')
            full_picture = schiaparelli_picture.find('a')['href']
            
schiaparelli_title = soup.find('h2', class_='title').text()

schiaparelli_hemisphere = {"Title":schiaparelli_title ,   "url":full_picture}

print(schiaparelli_hemisphere)
hemisphere_image_urls.append(schiaparelli_hemisphere)
url='https://astrogeology.usgs.gov/search/map/Mars/viking/syrtis_Major_enhanced'
response=requests.get(url)
soup=bs(response.text,'html.parser')
print(soup.prettify)
syrtis_Major_image=soup.find_all('div',class_='wide-image-wrapper')
for image in syrtis_Major_image:
            syrtis_Major_picture=image.find('li')
            full_picture = syrtis_Major_picture.find('a')['href']
            
syrtis_Major_title = soup.find('h2', class_='title').text()

syrtis_Major_hemisphere = {"Title":syrtis_Major_title ,   "url":full_picture}

print(syrtis_Major_hemisphere)
hemisphere_image_urls.append(syrtis_Major_hemisphere)

url='https://astrogeology.usgs.gov/search/map/Mars/viking/valles_Marineris_enhanced'
response=requests.get(url)
soup=bs(response.text,'html.parser')

valles_Marineris_image=soup.find_all('div',class_='wide-image-wrapper')

for image in valles_Marineris_image:
            valles_Marineris_picture=image.find('li')
            full_picture = valles_Marineris_picture.find('a')['href']
            
valles_Marineris_title = soup.find('h2', class_='title').text()

valles_Marineris_hemisphere = {"Title":valles_Marineris_title ,   "url":full_picture}

print(valles_Marineris_hemisphere)
hemisphere_image_urls.append(valles_Marineris_hemisphere)

hemisphere_image_urls

