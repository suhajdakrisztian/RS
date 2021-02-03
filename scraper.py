import praw
import pandas as pd
from datetime import datetime
from symbol_lists import SYMBOL_LIST

POST_LIMIT = 150
SUB_REDDIT = "Wallstreetbets"


class Credentials:

  def __init__(self):
    self.ID = "dYHJ4gMsuTV50A"
    self.SECRET = "kYYLp-LEYDAEFGYVc04lpXhr_d3qxQ"
    self.AGENT = "my_user_agent"


class DataCollector(Credentials):

  def __init__(self):
    super().__init__()
    self.main_dataframe = pd.DataFrame(columns = ["title", "score", "created"])
    self.split_title_list = []
    self.hot_stocks = []

  def scrape_reddit(self):

    reddit = praw.Reddit(client_id=self.ID, client_secret=self.SECRET, user_agent=self.AGENT)
    hot_posts = reddit.subreddit(SUB_REDDIT).hot(limit = POST_LIMIT)

    for post in hot_posts:
      self.main_dataframe = (self.main_dataframe).append({"title" : post.title,
                                                          "score" : post.score,
                                                          "created" : post.created}, ignore_index = True)

    (self.main_dataframe).sort_values(inplace= True, by= "score", ascending = False)
    (self.main_dataframe)["created"] = pd.to_datetime((self.main_dataframe)["created"], unit='s')
  
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
  scraper = DataCollector()
  scraper.scrape_reddit()
  scraper.split_titles()
  scraper.get_stocks()
  scraper.peek_stocks()
