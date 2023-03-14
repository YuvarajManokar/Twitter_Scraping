
![Logo](https://fiverr-res.cloudinary.com/images/q_auto,f_auto/gigs/189190529/original/409855f58d60400d22bdeb3251aace0a31fcdd85/do-effective-tweets-hashtags-followers-and-twitter-scraping.jpeg)

# What is Twitter Scraping?
Scraping is a technique to get information from Social Network sites. Scraping Twitter can yield many insights into sentiments, opinions and social media trends. Analysing tweets, shares, likes, URLs and interests is a powerful way to derive insight into public conversations. It is legal to scrape Twitter or any other SNS(Social Networking Sites) to extract publicly available information, but you should be aware that the data extracted might contain personal data.

# How to Scrape the Twitter Data?
Scraping can be done with the help of many opensource libraries like

- Tweepy
- Twint
- Snscrape
- Getoldtweets3

For my project I have used SNSCRAPE library.

# Libraries and Modules needed for the project!
snscrape.modules.twitter - (To Scrape the Data from Twitter)
- Pandas - (To Create a DataFrame with the scraped data)
- Pymongo - (To upload the dataframe to MongoDB database)
- Streamlit - (To Create Graphical user Interface)
- Datetime - (To get the current date)
- PIL - (To get the Image)

# Snscrape
Snscrape allows you to scrape basic information such as a user's profile, tweet content, source, and so on. Snscrape is not limited to Twitter, but can also scrape content from other prominent social media networks like Facebook, Instagram, and others. Its advantages are that there are no limits to the number of tweets you can retrieve or the window of tweets (that is, the date range of tweets). So Snscrape allows you to retrieve old data.

To know more about Snscrape do visit the official site-https://medium.com/dataseries/how-to-scrape-millions-of-tweets-using-snscrape-195ee3594721

# Streamlit
Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc. Streamlit allows you to re-use any Python code you have already written. This can save considerable amounts of time compared to non-Python based tools where all code to create visualizations needs to be re-written.

In my project I've extensively used streamlit API Reference feature for creation of Titles, Images, Headers, Input boxes, Buttons, Checkbox, Download buttons.

To know more about Streamlit do visit the official site- https://docs.streamlit.io/library/api-reference

# Workflow
Lets us see the workflow of the twitter scraping project by breakingdown it step by step.

To view the demo video of my project checkout this link - https://www.linkedin.com/in/yuvaraj-manokar-30294b16b/

# Step 1
Importing the libraries. As I have already mentioned above the list of libraries/modules needed for the project. First we have to import all those libraries. Before that check if the libraries are already installed or not by using the below piece of code.

    !pip install ["Name of the library"]

If the libraries are already installed then we have to import those into our script by mentioning the below codes.

    import snscrape.modules.twitter as sntwitter
    import pandas as pd
    import pymongo
    from pymongo import MongoClient
    from datetime import date
    import streamlit as st
    from PIL import Image

# Step 2
Import suitable image for the title and  Explain about the project use streamlit as st.

Twitter Scraping:  
This app is a Twitter  Scraping web app created using Streamlit.  It scrapes the twitter data  for the given hashtag/keyword for the given period. The tweets are uploaded in MongoDB and can be downloaded as CSV or a JSON file.

    # twitter scraping image,Titles and sub-heading
    image = Image.open("twitter.JPG")
    st.image(image, caption="Scrape Tweets with any keywords or Hashtag as you wish!")
    st.write('''This app is a Twitter  Scraping web app created using **:blue[Streamlit]**.  It scrapes the twitter data  for the given **:blue[hashtag/keyword]** for the given period. The tweets are uploaded in **:blue[MongoDB]** and can be downloaded as **:blue[CSV or a JSON]** file.''')

# Step 3
Give Subheader & By using Expander syntax to explain about Snscrape, streamlit, MongoDB & twitter Scrape use streamlit as st.

Twitter Scrape:  
Twitter Scraper will scrape the data from Public Twitter profiles. It will collect the data about date, id, url, tweet content, users/tweeters, reply count, retweet count, language, source, like count, followers, friends and lot more information to gather the real facts about the Tweets.

Snscrape:  
Snscraper is a scraper for social media services like twitter, facebook, instagram and so on. It scrapes user profiles, hashtag, other tweet information and returns the discovered items from the relevant posts/tweets.

Streamlit:  
Streamlit is a awesome opensource framework used for building highly interactive sharable web application in python language. It's easy to share machine learning and datascience web apps using streamlit. It allows the app to load the large set of data's from web for manipulation and performing expensive computations.

MongoDB:  
MongoDB is an open source document database used for storing unstructured data. The data is stored as JSON like documents called BSON. It is used by developers to work easily with real time data analytics, content management and lot of other web applications.

    # About Twitter scraper, Snscraper, Streamlit, MongoDB
    st.subheader(":blue[About]")
    with st.expander("**Twitter Scraper**"):
        st.write('''Twitter Scraper will scrape the data from Public Twitter profiles.It will collect the data about **:blue[date, id, url, tweet content, users/tweeters, reply count,retweet count, language, source, like count, followers, friends]** and lot more information to gather the real facts about the Tweets.''')

    with st.expander("**Snscraper**"):
        st.write('''Snscraper is a scraper for social media services like *:blue[twitter, facebook, instagram and so on.]* It scrapes **:blue[user profiles, hashtag, other tweet information]** and returns the discovered items from the relevant posts/tweets.''')

    with st.expander("**MongoDB**"):
        st.write('''MongoDB is an open source document database used for storing unstructured data. **:blue[The data is stored as JSON like documents called BSON.]** It is used by developers to work easily with real time data analytics, content management and lot of other web applications''')

    with st.expander("**Streamlit**"):
        st.write('''Streamlit is a **:blue[awesome opensource framework used for building highly interactive sharable web application]** in python language. It's easy to share *:blue[machine learning and datascience web apps]* using streamlit. It allows the app to load the large set of data's from web for manipulation and performing expensive computations.''')

# Step 4
Give subheader of the Variable declaration for user inputs(Keyword and Number of tweets)

    # Variable declaration for user inputs(Keyword and Number of tweets)
    st.subheader(":blue[Kindly fill the below details to begin Scraping Tweets] :point_down:")

Getting inputs from the user. In the below code I have created the list of variables for getting user input. With the help of streamlit I've also created the input boxes like text_input, number_input, date_input.

Keyword or Hashtag the user needed to search for (hashtag)
Tweets posted since date (since)
Tweets posted until date (until)
Number of tweets the user wants to scrape (maxTweets)

    hashtag = st.text_input("Enter the keyword or Hashtag you need to get : ")
    date = st.write("**:blue[Select the date range] :calendar:**")
    since = st.date_input('Start date (YYYY-MM-DD) : ')
    until = st.date_input('End date (YYYY-MM-DD) : ')
    maxTweets = st.slider('Enter the number of Tweets to Scrape :', 0,1000,100)
    maxTweets = int(maxTweets)

# Step 5
After getting user inputs. In the next step I've created an empty list (tweets_list) so that we are going to append the scraped tweets from the twitter. Then with the streamlit library I've created the button(Submit).

With the help of for loop and enumerate function im getting the variety of information from twitter. The method I've used is sntwitter.TwitterSearchScraper which helps in getting informations like date, id, rawContent, username, replyCount, retweetCount, likeCount, language, source and etc.

The loop will run till the iteration reaches the count provided b the user. Then these details are getting appended to the list called (tweets_list).The tweets will only get scraped if the proper input is provided.

The First button for submit the user input

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

# Step 6
- The first function is used to create the Pandas DataFrame using the datas that was appended to tweets_list = []. Column names were provided as per my need.
- Second function is to convert the DataFrame object into a CSV file using to_csv() function.
- The last function is to convert the DataFrame object into a JSON file using to_json() function.

        # Creating DataFrame with the scraped tweets   
        def data_frame(data):
            return pd.DataFrame(data, columns= ['datetime', 'user_id', 'url', 'tweet_content', 'user_name','reply_count', 'retweet_count', 'like_count', 'language', 'source'])

        # Converting DataFrame to CSV file
        def convert_to_csv(c):
            return c.to_csv().encode('utf-8')

        # Converting DataFrame to JSON file
        def convert_to_json(j):
            return j.to_json(orient='index')

Here is the object creation with different variable names of all the above three functions. This will act as the driver code for function execution.

    # Creating objects for dataframe and file conversion
    df = data_frame(tweets_list)
    csv = convert_to_csv(df)
    json = convert_to_json(df)

# Step 7
Bridging the connection between MongoDB and Python. For this we would need the pymongo library and the .MongoClient attribute. After successful connection I've created the database named GUVI_P1_Twitter_Scraping and collection named {hashtag}-tweet. We are going to store all the scraped datas in this collection.

The scr_data is going to hold the basic informations like Scraped wordand scraped data. Then these details are uploded into the MongoDB collection.

    # Bridging a connection with MongoDB Atlas and Creating a new database(twitterscraping) and collections(scraped_data)
    client = pymongo.MongoClient("mongodb+srv://Yuvaraj:12345@cluster0.vz1nuky.mongodb.net/?retryWrites=true&w=majority")
    db = client.GUVI_P1_Twitter_Scraping
    col = db[f"{hashtag}_tweet"]
    scr_data = {"Scraped_word" : hashtag,
                "Scraped_data" : df.to_dict('records')
                }

# Step 8
Here comes the importance of streamlit in my project. I have created four buttons overall for this project.

Give subheader to view the DataFrame 

The Second button is used to view the dataframe. Once the user clicks this button the df function is called and then dataframe will appear in the screen along with the success message as ✅DataFrame Fetched Successfully.

    # BUTTON 2 - To view the DataFrame
    st.subheader(":blue[:point_down: To display the data use the below button]")
    if st.button("Display Tweets"):
        st.success(f"Tweet #{hashtag} DataFrame Fetched Successfully :point_down:", icon="✅")
        st.write(df)

# Step 9

Once the Upload the data to MongoDB button is clicked by the user the scr_data which we have already created is getting uploaded to the MongoDB collection. Then the new records is getting inserted with the help of insert_one function. And finally the user will get the success message ✅Upload to MongoDB Successful! in their screen.

If the user clicks this button without scraping the data the error message will be popped like You cannot upload an empty dataset. Kindly enter all the information in the above user input.

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

# Step 10
The simple streamlit subheader that denotes the downloading options of the scraped data.

    # Header Diff Options to download the dataframe
    st.subheader(":blue[To Download data as CSV & JSON use the below buttons :arrow_down:]")

For giving the download button to split the column into 4 for two download button in mid of frame

    # split the column into 4 for giving two download button in mid of frame
    col1, col2, col3, col4 = st.columns(4)

    image = Image.open("CSV.PNG")
    col2.image(image)

    image = Image.open("JSON.JPG")
    col3.image(image)

# Step 11

These below two buttons are used to generate CSV or JSON files as per the user wish. In the backend the conver_to_csv or conver_to_json is called and executed. User will get the CSV file or JSON file downloaded to their downloads.

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

# Step 12
To run this script go to the Terminal and type the below command, you will get a new window opened in your browser there we can interact with the streamlit user interface.

	streamlit run Twitter_Scraping.py