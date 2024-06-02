import streamlit as st
import pandas as pd
from ntscraper import Nitter
from tqdm import tqdm


from tqdm import tqdm

class Nitter:
    def __init__(self, disable_tqdm=True):
        self.disable_tqdm = disable_tqdm
        # Initialize instances (example, you might have actual code here)
        self.instances = []  # This should be your actual initialization
        # other initialization code

    def _test_all_instances(self, path, no_print=False):
        for instance in tqdm(self.instances, desc="Testing instances", disable=self.disable_tqdm):
            # testing code
            pass






# Function to scrape tweets
def scrape_tweets(username, mode, number, disable_tqdm=True):
    sc = Nitter(disable_tqdm=disable_tqdm)
    tweets = sc.get_tweets(username, mode=mode, number=number)
    final = []
    for tweet in tweets['tweets']:
        data = [tweet['date'], tweet['link'], tweet['text'], tweet['stats']['comments'], tweet['stats']['retweets'], tweet['stats']['quotes'], tweet['stats']['likes'], tweet['user']['avatar']]
        final.append(data)
    df = pd.DataFrame(final, columns=['date','link', 'text', 'comments', 'retweets', 'quotes', 'likes', 'avatar'])
    return df

# Streamlit app
st.title("Twitter Scraper")

# Input fields
username = st.text_input("Enter Twitter Username:")
mode = st.selectbox("Select Mode:", ["user", "hashtag", "term"])
number = st.number_input("Number of Tweets to Scrape:", value=10)

# Button to scrape tweets
if st.button("Scrape Tweets"):
    if username:
        with st.spinner("Scraping tweets..."):
            df = scrape_tweets(username, mode, number)
            st.success("Tweets scraped successfully!")
            
            # Displaying the DataFrame with clickable and expandable text
            for index, row in df.iterrows():
                with st.expander(f"Tweet {index + 1}: Click to expand"):
                    st.write(f"**Date**: {row['date']}")
                    st.write(f"**Text**: {row['text']}")
                    st.write(f"**Comments**: {row['comments']}")
                    st.write(f"**Retweets**: {row['retweets']}")
                    st.write(f"**Quotes**: {row['quotes']}")
                    st.write(f"**Likes**: {row['likes']}")
                    st.write(f"**Link**: [Tweet Link]({row['link']})")
                    st.image(row['avatar'], width=50)
    else:
        st.error("Please enter a Twitter username.")
