import pandas as pd
import requests
import time
from datetime import date
from bs4 import BeautifulSoup as soup
from urllib.request import Request, urlopen
import streamlit as st
import base64
import json
#from pandas.json_normalize import json_normalize # Will return with more documentation
#import feedparser
import xml.etree.ElementTree as ET



ts = int(time.time())
today = date.today()
print(today)
#st.write(today)

st.title('ContentCharts Web-Application')
st.write("""You are visiting on:    """ + str(today))
#sidebar_selection = st.sidebar.radio(
#    'Select location data to display:',
#    ['Show Global', 'Show U.S', 'Show U.K', 'Show other'],
#)


#sidebar_selection = st.sidebar.radio(
#    'Select music platform chart data to display:',
#    ['Show All', 'Show Apple Music', 'Show iTunes Store (Music)', 'Show none'],
#)

#sidebar_selection = st.sidebar.radio(
#    'Select movie platform chart data to display:',
#    ['Show All', 'Show iTunes Store (Movies/AppleTV)', 'Show none'],
#)

#sidebar_selection = st.sidebar.radio(
#    'Select podcast platform chart data to display:',
#    ['Show All', 'Show Apple Podcasts', 'Show none'],
#)

#sidebar_selection = st.sidebar.radio(
#    'Select app platform chart data to display:',
#    ['Show All', 'Show App Store', 'Show none'],
#)


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




#data = []
#for url in rss_urls:
#    response = requests.get(url).json()
#    entries = response['feed']['results']
#    for results in rss_urls:
#        data.append({
#            'type': results['contentType']['attributes']['label'],
#            'title': results['title']['label'],
#            'artist': results['im:artist']['label'],
#            'release_date': results['im:releaseDate']['label'],
#            'price': results.get('im:price', {}).get('label', ''),
#            'link': results['link']['attributes']['href']
#        })

#for url in rss_urls:
    #response = requests.get(url)
    #root = ET.fromstring(response.text)

    #for item in root.iter('title'):
        #print(item.find('title').text)


#sidebar_selection = st.sidebar.radio(
    #'Select location data to display:',
    #['Show All', 'Show Apple Music', 'Show iTunes Store (Music)', 'Show App Store',
# 'Show iTunes Store (Movies)(Apple TV), 'Show iTunes Store (TV Shows)(Apple TV)],)


# Apple Music (United States)
def get_data():
    Played_songs = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json'
    Played_albums ='https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/albums.json'
    playedsongs = pd.read_json(Played_songs)
    playedalbums = pd.read_json(Played_albums)
    Played_playlists = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/playlists.json'
    playedplaylists = pd.read_json(Played_playlists)
    Played_mvs = 'https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/music-videos.json'
    playedmvs = pd.read_json(Played_mvs)

    return playedsongs, playedalbums, playedplaylists, playedmvs

playedsongs, playedalbums, playedplaylists, playedmvs = get_data()


print("-----Apple Music Charts (Top 100)-----")
print("**Top songs actively played " + str(playedsongs))
print("**Top albums actively played " + str(playedalbums))
print("**Top playlists actively played " + str(playedplaylists))
print("**Top Music Videos actively played " + str(playedmvs))

st.header("Apple Music Charts (Top 100)")
st.subheader("**Top songs actively played** " + str(playedsongs))
st.subheader("**Top albums actively played** " + str(playedalbums))
st.subheader("**Top playlists actively played** " + str(playedplaylists))
st.subheader("**Top Music Videos actively played** " + str(playedmvs))


# iTunes Store Music (United States)
def get_data():
    Top_songs = 'https://itunes.apple.com/us/rss/topsongs/limit=100/explicit=true/json'
    topsongs = pd.read_json(Top_songs)
    Top_albums = 'https://itunes.apple.com/us/rss/topalbums/limit=100/explicit=true/json'
    topalbums = pd.read_json(Top_albums)
    Top_mvs = 'https://itunes.apple.com/us/rss/topmusicvideos/limit=100/explicit=true/json'
    topmvs = pd.read_json(Top_mvs)

    return topsongs, topalbums, topmvs



topsongs, topalbums, topmvs = get_data()
print("-----iTunes Store Music Charts (Top 100)-----")
print("**Top songs actively purchased " + str(topsongs))
print("**Top albums actively purchased " + str(topalbums))
print("**Top Music Videos actively purchased " + str(topmvs))

st.header("iTunes Store Music Charts (Top 100)")
st.subheader("**Top songs actively purchased** " + str(topsongs))
st.subheader("**Top albums actively purchased** " + str(topalbums))
st.subheader("**Top Music Videos actively purchased** " + str(topmvs))

#App Store (United States)
# Top Free, Paid Apps
def get_data():
    Top_free = 'https://rss.applemarketingtools.com/api/v2/us/apps/top-free/50/apps.json'
    topfree = pd.read_json(Top_free)
    Top_paid = 'https://rss.applemarketingtools.com/api/v2/us/apps/top-paid/50/apps.json'
    toppaid = pd.read_json(Top_paid)

    return topfree, toppaid

topfree, toppaid = get_data()
print("-----App Store Charts (Top 100)-----")
print("**Top free apps actively downloaded " + str(topfree))
print("**Top paid apps actively purchased " + str(toppaid))

st.header("App Store Charts (Top 100)")
st.subheader("**Top free apps actively downloaded** " + str(topfree))
st.subheader("**Top paid apps actively purchased** " + str(toppaid))


# iTunes Store Movies (AppleTV) (United States)
def get_data():
    Top_movies = 'https://itunes.apple.com/us/rss/topmovies/limit=100/explicit=true/json'
    topmovies = pd.read_json(Top_movies)

    return topmovies
topmovies = get_data()
print("-----iTunes Store Movies (AppleTV) Charts (Top 100)-----")
print("**Top movies actively purchased " + str(topmovies))


st.header("iTunes Store Movies (AppleTV) Charts (Top 100)")
st.subheader("**Top movies actively purchased** " + str(topmovies))


# Apple Podcasts (United States)
def get_data():
    Top_podcasts = 'https://rss.applemarketingtools.com/api/v2/us/podcasts/top/100/podcasts.json'
    toppodcasts = pd.read_json(Top_podcasts)
    Top_podeps = 'https://rss.applemarketingtools.com/api/v2/us/podcasts/top/100/podcast-episodes.json'
    toppodeps = pd.read_json(Top_podeps)
    Top_podsubs = 'https://rss.applemarketingtools.com/api/v2/us/podcasts/top-subscriber/50/podcast-channels.json'
    toppodsubs = pd.read_json(Top_podsubs)


    return toppodcasts, toppodeps, toppodsubs

toppodcasts, toppodeps, toppodsubs = get_data()
print("-----Apple Podcasts Charts (Top 100)-----")
print("**Top podcasts actively listened to " + str(toppodcasts))
print("**Top podcast episodes actively listened to " + str(toppodeps))
print("**Top podcasts actively subscribed to " + str(toppodsubs))



st.header("Apple Podcasts Charts (Top 100)")
st.subheader("**Top podcasts actively listened to** " + str(toppodcasts))
st.subheader("Top podcast episodes actively listened to " + str(toppodeps))
st.subheader("Top podcasts actively subscribed to " + str(toppodsubs))

