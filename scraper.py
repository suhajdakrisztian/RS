import praw
import pandas as pd
import nltk
from datetime import datetime
from symbol_lists import SYMBOL_LIST


"""
TODO:
x Map ticker to company names and return them
x use NLP for contextual analysis
x fix time-traveling (see main_dataframe["created"])
x Figure out calling Python in C++ for making a "one-click" app
"""

API_ID = "dYHJ4gMsuTV50A"
API_SECRET = "kYYLp-LEYDAEFGYVc04lpXhr_d3qxQ"
API_AGENT = "my_user_agent"

POST_LIMIT = 150
SUB_REDDIT = "Wallstreetbets"

class Credentials():
  def __init__(self):
    self.API_ID = "dYHJ4gMsuTV50A"
    self.API_SECRET = "kYYLp-LEYDAEFGYVc04lpXhr_d3qxQ"
    self.API_AGENT = "my_user_agent"


class DataCollector():

  def __init__(self):
    super().__init__()
    self.main_dataframe = pd.DataFrame(columns = ["title", "score", "created"])
    self.split_title_list = []
    self.hot_stocks = []

  def scrape_reddit(self, credential_object):

    reddit = praw.Reddit(client_id = credential_object.API_ID,
                         client_secret = credential_object.API_SECRET,
                         user_agent = credential_object.API_AGENT)

    hot_posts = reddit.subreddit(SUB_REDDIT).hot(limit = POST_LIMIT)

    for post in hot_posts:
      self.main_dataframe = self.main_dataframe.append({"title" : post.title,
                                                        "score" : post.score,
                                                        "created" : post.created}, ignore_index = True)

    self.main_dataframe.sort_values(by= "score", ascending = False, inplace= True)
    self.main_dataframe["created"] = pd.to_datetime(self.main_dataframe["created"], unit='s')
  
  def split_titles(self):

    for title in self.main_dataframe["title"]:
      self.split_title_list.append(title.split(" "))
  
  def get_stocks(self):
    for title in self.split_title_list:
      for word in title:
        if word in SYMBOL_LIST:
          self.hot_stocks.append(word)

    self.hot_stocks = list(set(self.hot_stocks))

  def peek_dataframe(self):
    print(self.main_dataframe)
  
  def peek_stocks(self):
    print(self.hot_stocks)

def run_scraper():

  creds = Credentials()
  scraper = DataCollector()

  scraper.scrape_reddit(creds)
  scraper.split_titles()
  scraper.get_stocks()
  scraper.peek_stocks()
