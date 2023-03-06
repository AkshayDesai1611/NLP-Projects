# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 17:54:59 2021

@author: LENOVO
"""

import requests   # Importing requests to extract content from a url
from bs4 import BeautifulSoup as bs # Beautifulsoup is for web scrapping...used to scrap specific content 
import re 
import tweepy

import matplotlib.pyplot as plt
from wordcloud import WordCloud

KGF1_reviews = []

#for i in range(1,21):
    
    
    
  i = 0 
  ip=[]  
  url="https://www.imdb.com/title/tt7838252/reviews?ref_=tt_urv"+str(i)
  response = requests.get(url)
  soup = bs(response.content,"html.parser")# creating soup object to iterate over the extracted content 
  reviews = soup.find_all("div",class_="text show-more__control")# Extracting the content under specific tags  
  for i in range(len(reviews)):
    ip.append(reviews[i].text)  
 
  KGF1_reviews=KGF1_reviews+ip
  
  # writng reviews in a text file 
with open("KGF_reviews.txt","w",encoding='utf8') as output:
    output.write(str(KGF1_reviews))

# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(KGF1_reviews)

import nltk
# from nltk.corpus import stopwords


# Removing unwanted symbols incase if exists
ip_rev_string = re.sub("[^A-Za-z" "]+"," ", ip_rev_string).lower()
ip_rev_string = re.sub("[0-9" "]+"," ", ip_rev_string)


# words that contained in iphone XR reviews
ip_reviews_words = ip_rev_string.split(" ")

#TFIDF
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(ip_reviews_words, use_idf=True,ngram_range=(1, 3))
X = vectorizer.fit_transform(ip_reviews_words)

with open("C:/Users/LENOVO/Desktop/360/Text Mining and NLP/stop.txt","r") as sw:
    stop_words = sw.read()
    
stop_words = stop_words.split("\n")

stop_words.extend(["yash","rocking","star","awesome","kannada","movie","prashant","sandalwood","neel","bhai","mumbai","gold","adhira"])

ip_reviews_words = [w for w in ip_reviews_words if not w in stop_words]


# Joinining all the reviews into single paragraph 
ip_rev_string = " ".join(ip_reviews_words)

# WordCloud can be performed on the string inputs.
# Corpus level word cloud

wordcloud_ip = WordCloud(
                      background_color='White',
                      width=1800,
                      height=1400
                     ).generate(ip_rev_string)

plt.imshow(wordcloud_ip)

# positive words # Choose the path for +ve words stored in system
with open("C:/Users/LENOVO/Desktop/360/Text Mining and NLP/positive-words.txt","r") as pos:
  poswords = pos.read().split("\n")


# Positive word cloud
# Choosing the only words which are present in positive words
ip_pos_in_pos = " ".join ([w for w in ip_reviews_words if w in poswords])

wordcloud_pos_in_pos = WordCloud(
                      background_color='White',
                      width=1800,
                      height=1400
                     ).generate(ip_pos_in_pos)
plt.figure(2)
plt.imshow(wordcloud_pos_in_pos)

# negative words Choose path for -ve words stored in system
with open("C:/Users/LENOVO/Desktop/360/Text Mining and NLP/negative-words.txt", "r") as neg:
  negwords = neg.read().split("\n")

# negative word cloud
# Choosing the only words which are present in negwords
ip_neg_in_neg = " ".join ([w for w in ip_reviews_words if w in negwords])

wordcloud_neg_in_neg = WordCloud(
                      background_color='black',
                      width=1800,
                      height=1400
                     ).generate(ip_neg_in_neg)
plt.figure(3)
plt.imshow(wordcloud_neg_in_neg)




