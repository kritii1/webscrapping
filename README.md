# webscrapping
import requests
from bs4 import BeautifulSoup
import pandas as pd

page= requests.get('https://realpython.github.io/fake-jobs/')
soup=BeautifulSoup(page.content,'html.parser')

