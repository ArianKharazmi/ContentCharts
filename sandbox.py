import pandas as pd
import requests
import time
from datetime import date
import streamlit as st

ts = int(time.time())
today = date.today()
print(today)

st.title('ContentCharts Web-Application')
st.write("""You are visiting on:    """ + str(today))

rss_urls = [
    # AM Most Played Songs
    'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json',
    # AM Most Played Albums
    'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/albums.json',
    # AM Most Played Playlists
    'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/playlists.json',
    # AM Most Played Music Videos
    'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/music-videos.json',
    # iTunes Most Actively Bought Songs
    'https://itunes.apple.com/us/rss/topsongs/limit=100/explicit=true/json',
    # iTunes Most Actively Bought Albums
    'https://itunes.apple.com/us/rss/topalbums/limit=100/explicit=true/json',
    # iTunes Most Actively Bought Music Videos
    'https://itunes.apple.com/us/rss/topmusicvideos/limit=100/explicit=true/json'
]

st.write()