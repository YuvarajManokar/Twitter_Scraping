# importing libraries and modules needed for the project
import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
from pymongo import MongoClient
from datetime import date
import streamlit as st
from PIL import Image


# twitter scraping image,Titles and sub-heading
image = Image.open("twitter.JPG")
st.image(image, caption="Scrape Tweets with any keywords or Hashtag as you wish!")
st.write('''This app is a Twitter  Scraping web app created using **:blue[Streamlit]**.  It scrapes the twitter data  for the given **:blue[hashtag/keyword]** for the given period. The tweets are uploaded in **:blue[MongoDB]** and can be downloaded as **:blue[CSV or a JSON]** file.''')


# About Twitter scraper, Snscraper, Streamlit, MongoDB
st.subheader(":blue[About]")
with st.expander("**Twitter Scraper**"):
    st.write('''Twitter Scraper will scrape the data from Public Twitter profiles.
                    It will collect the data about **:blue[date, id, url, tweet content, users/tweeters, reply count,
                    retweet count, language, source, like count, followers, friends]** and lot more information
                    to gather the real facts about the Tweets.''')

with st.expander("**Snscraper**"):
    st.write('''Snscraper is a scraper for social media services like *:blue[twitter, facebook, instagram and so on.]* It scrapes
                    **:blue[user profiles, hashtag, other tweet information]** and returns the discovered items from the
                    relevant posts/tweets.''')

with st.expander("**MongoDB**"):
    st.write('''MongoDB is an open source document database used for storing unstructured data. **:blue[The data is
                    stored as JSON like documents called BSON.]** It is used by developers to work easily with real time
                    data analytics, content management and lot of other web applications''')

with st.expander("**Streamlit**"):
    st.write('''Streamlit is a **:blue[awesome opensource framework used for building highly interactive sharable web
                    application]** in python language. It's easy to share *:blue[machine learning and datascience web apps]* using
                    streamlit. It allows the app to load the large set of data's from web for manipulation and performing
                    expensive computations.''')


# Variable declaration for user inputs(Keyword and Number of tweets)
st.subheader(":blue[Kindly fill the below details to begin Scraping Tweets] :point_down:")

hashtag = st.text_input("Enter the keyword or Hashtag you need to get : ")
date = st.write("**:blue[Select the date range] :calendar:**")
since = st.date_input('Start date (YYYY-MM-DD) : ')
until = st.date_input('End date (YYYY-MM-DD) : ')
maxTweets = st.slider('Enter the number of Tweets to Scrape :', 0,1000,100)
maxTweets = int(maxTweets)

# Creating an empty list
tweets_list = []
# Enabling the Checkbox only when the hashtag is entered
if hashtag:
    # Button - 1 for submit the user input
    if st.button('Submit'):
        st.success(f"Tweet #{hashtag} received for scraping successfully", icon="✅")
    # Using for loop, TwitterSearchScraper and enumerate function to scrape data and append tweets to list
    passing = f"{hashtag} since:{since} until:{until}"
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(passing).get_items()):
        if i > maxTweets:
            break
        tweets_list.append([tweet.date,
                            tweet.id,
                            tweet.url,
                            tweet.rawContent,
                            tweet.user.username,
                            tweet.replyCount,
                            tweet.retweetCount,
                            tweet.likeCount,
                            tweet.lang,
                            tweet.source
                            ])

else:
    st.button("Submit",disabled=True)

# Creating DataFrame with the scraped tweets
def data_frame(data):
    return pd.DataFrame(data, columns= ['datetime', 'user_id', 'url', 'tweet_content', 'user_name',
                                        'reply_count', 'retweet_count', 'like_count', 'language', 'source'])

# Converting DataFrame to CSV file
def convert_to_csv(c):
    return c.to_csv().encode('utf-8')

# Converting DataFrame to JSON file
def convert_to_json(j):
    return j.to_json(orient='index')


# Creating objects for dataframe and file conversion
df = data_frame(tweets_list)
csv = convert_to_csv(df)
json = convert_to_json(df)


# Bridging a connection with MongoDB Atlas and Creating a new database(twitterscraping) and collections(scraped_data)
client = pymongo.MongoClient("mongodb+srv://Yuvaraj:12345@cluster0.vz1nuky.mongodb.net/?retryWrites=true&w=majority")
db = client.GUVI_P1_twitter_Scraping
col = db[f"{hashtag}_tweet"]
scr_data = {"Scraped_word" : hashtag,
            "Scraped_data" : df.to_dict('records')
           }
'\n' # Next line
"\n" # Next line

# BUTTON 2 - To view the DataFrame
st.subheader(":blue[:point_down: To display the data use the below button]")
if st.button("Display Tweets"):
    st.success(f"Tweet #{hashtag} DataFrame Fetched Successfully :point_down:", icon="✅")
    st.write(df)

'\n' # Next line
'\n' # Next line

# BUTTON 3 - To upload the data to mongoDB database
st.subheader(":blue[:point_down: To Upload the data to MongoDB use the below button]")

image = Image.open("MongoDB.PNG")
st.image(image)

if st.button("Upload the data"):
    try:
        col.insert_one(scr_data)
        st.success(f'Tweet #{hashtag} Successfully Upload to MongoDB', icon="✅")
        st.balloons()
        collections = db.list_collection_names()
        st.write("List of collection that already exists : ")
        # for i in collections:
        st.write(collections)

    except:
        st.error('You cannot upload an empty dataset. Kindly enter all the information in the above user input.', icon="🚨")

"\n" # Next line
"\n" # Next line

# Header Diff Options to download the dataframe
st.subheader(":blue[To Download data as CSV & JSON use the below buttons :arrow_down:]")

# split the column into 4 for giving two download button in mid of frame
col1, col2, col3, col4 = st.columns(4)

image = Image.open("CSV.PNG")
col2.image(image)

image = Image.open("JSON.JPG")
col3.image(image)


# BUTTON 4 - To download data as CSV
if col2.download_button(label= "Download",
                        data= csv,
                        file_name= f'{hashtag} scraped_tweets_data.csv',
                        mime= 'text/csv'
                        ):
    st.success("Successfully Downloaded data as CSV")

# BUTTON 5 - To download data as JSON
if col3.download_button(label= "Download",
                        data= json,
                        file_name= f' {hashtag} scraped_tweets_data.json',
                        mime= 'text/csv'
                        ):
    st.success("Successfully Downloaded data as JSON")
