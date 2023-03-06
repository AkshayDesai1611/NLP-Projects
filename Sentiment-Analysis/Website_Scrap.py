# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 23:31:48 2021

@author: LENOVO
"""


import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 
#import tweepy
import pandas 
from yt_stats import YTstats
from tqdm import tqdm



import matplotlib.pyplot as plt
from wordcloud import WordCloud

Modi_reviews = []

  i = 0 
  ip=[]  
  url="https://www.youtube.com/watch?v=XUqQEbLVot0"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.find_all("span",attrs={"class","style-scope yt-formatted-string"})# Extracting the content under specific tags  
  for i in range(len(reviews)):
      ip.append(reviews[i].text
      
  