# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 06:06:47 2018

@author: dglen
"""
#Installs
#pip install cython, numpy, pandas, matplotlib, keras, tensorflow, lxml, BeautifulSoup4, textblob

# Imports
import pandas as pd
#from io import StringIO
import time
import requests
# Froms
import matplotlib.pyplot as plt
#%matplotlib inline #The next two lines are pure python that also works in Spyder
#from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'qt')
#from lxml import etree
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from textblob import TextBlob
#import sys
#from PyQt4 import QtGui, QtCore
#from PyQt4.QtGui import *

#import numpy as np
#import keras
#import tensorflow as tf
#import urllib.request 
#import urllib.error 
#from keras.datasets import imdb
#from keras.models import Sequential
#from keras.layers import Dense, Dropout, Activation
#from keras.preprocessing.text import Tokenizer
#from io import BytesIO
#from io import StringIO
#from lxml import etree 
#from lxml import html 

# Global Variables
chrome_path = r"C:\Dave\UWF\COT6931-II\Sources\chromedriver.exe"
open_data_path_name = 'stock_records.csv'
save_data_path_name = 'stock_records.csv'
price_news_source_url = "https://stocknews.com/stock/TSLA/news/"
# Import the GUI. Doesn't appear to be needed
"""
class MainWindow():
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Window()
        self.ui.__init__(self.main_win)
        
    def show(self):
        self.main_win.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
"""
# Connect to the webpage, read the dynamic html provided by javaScript and load into a BeautifulSoup container
#print('Use of Google Chrome is required for this application. It also requires the latest chromedriver.exe')
#filename = 'stock_records.csv'
# Add function to select chromedriver.
def setChrome(chrome_path, price_news_source_url):
    driver = webdriver.Chrome(chrome_path)
    driver.get(price_news_source_url)
    time.sleep(30) #pauses for 30 seconds to manually login and to prevent IP blocking due to the quasi-legal nature of web-scraping
    no_of_pagedowns = 1 #20, Change this to a variable and show on the GUI.
    while no_of_pagedowns: # Load more news
        try:
            driver.find_element_by_xpath("//*[@id='load-more-button']").send_keys(Keys.ENTER)
            time.sleep(2)
            no_of_pagedowns-=1
        except Exception as e:
            print(e)
            break
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    #print(soup.prettify()) # HTML achieved
    return soup
    driver.quit()

# Locates the desired table and loads all records from the table rows to the record dataset
def scrapeIt(soup):
    table = soup.find('tbody', attrs = {'id':'snippets-tbody'}) 
    records = []
    count = 1
    for row in table.findAll('tr', attrs = {'style':''}): 
        record = {} 
        record['date'] = row.find('span', attrs = {'class':'medium-gray'}).text + ', 2018'
        record['url'] = 'https://stocknews.com' + row.find('td', attrs = {'data-title':'News Detail'}).a['href']
        record['price'] = row.find('td', attrs = {'class':'text-right'}).text 
        record['heading'] = row.find('span', attrs = {'class':'dark-gray'}).text
        record['heading_sentiment'] = inlineSA(record['heading'])
        record['body'] = pageScrapeOne('https://stocknews.com' + row.find('td', attrs = {'data-title':'News Detail'}).a['href'])
        record['body_sentiment'] = inlineSA(record['body'])
        records.append((record))
        print('Record ', count)
        count += 1
        time.sleep(3)
    return records

# Pandas DataFrame to CSV file
def toCSV(records, save_data_path_name):
    df = pd.DataFrame(records, columns=['date', 'heading', 'heading_sentiment', 'price', 'url', 'body', 'body_sentiment'])
    df['date'] = pd.to_datetime(df['date'])
    df.to_csv(save_data_path_name, index=False, encoding='utf-8')
    return

# Scraping all of the articles for full sentiment analysis
def pageScrapeOne(url):
    try:
        res = requests.get(url)
    except Exception as e:
        print("URL not found. Body text not harvested.", e)
        return    
    soup_body = BeautifulSoup(res.text,"lxml")
    article_text = ''
    article = soup_body.find("div", {"class":"post_content"}).findAll('p')
    for element in article:
        article_text += '\n' + ''.join(element.findAll(text = True))    
    res.close()
    time.sleep(5)
    return article_text

def inlineSA(text):
    testimonial = TextBlob(text)
    #Sentiment(polarity=0.39166666666666666, subjectivity=0.4357142857142857) - Sample
    sa = testimonial.sentiment.polarity # 0.39166666666666666 - sample
    if (sa >= -1 and sa <= -0.6):
        return 1
    elif (sa > -0.6 and sa <= -0.2):
        return 2
    elif (sa > 0.2 and sa <= 0.6):
        return 4
    elif (sa > 0.6 and sa <= 1.0):
        return 5
    return 3

# Display csv file
def printCSV(open_data_path_name):
    print(pd.read_csv(open_data_path_name))
    return

# Reading from a file. Exception handling moved to GUI
def setDataframe(filename):
    df = pd.read_csv(filename)
    df['date'] = pd.to_datetime(df['date'])
    return df

def correlate(df):
    x = df['date']
    y = df['price'].astype(float)
    z1 = df['heading_sentiment']
    #z2 = df['body_sentiment']
    # separate the figure object and axes object from the plotting object
    fig, ax1 = plt.subplots(figsize=(20,10))
    # duplicate the axes with a different y axis and the same x axis
    ax2 = ax1.twinx() # ax2 and ax1 with have a common x axis and different y axis
    # plot the curves on axes 1, and 2, and get the curve handles
    plt.xticks(rotation='vertical')
    curve1 = ax1.plot(x, y, label = 'Price', color = 'g')
    curve2 = ax2.plot_date(x, z1, label = 'Heading Sentiment', color = 'r', marker='*')
    #curve3 = ax2.plot_date(x, z2, label = 'Body Sentiment', color = 'c', marker='+')
    plt.title('Price and Sentiment Overlay')
    plt.xlabel('Date')
    plt.ylabel('News Sentiment / Price')
    ax1.legend(loc=2, shadow=True)
    ax2.legend(loc=1, shadow=True)
    plt.show()
    return

