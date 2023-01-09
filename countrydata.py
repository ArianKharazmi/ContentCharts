import pandas as pd
import requests
import time
from datetime import date
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import streamlit as st
import base64
import json
import pandas as pd
from pandas.io.json import json_normalize
#import feedparser
import xml.etree.ElementTree as ET
import main

# --------- Country Data






def get_data():
    Played_albums ='https://rss.applemarketingtools.com/api/v2/dz/music/most-played/50/albums.json'
    playedalbums = pd.read_json(Played_albums)

    return playedalbums

playedalbums = get_data()


print("-----Apple Music Charts Algeria (Top 100)-----")
print("**Top albums actively played " + str(playedalbums))