import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i, tweet in enumerate(
    sntwitter.TwitterSearchScraper(
        "Türkiye since:2021-11-1 until:2022-3-5"
    ).get_items()
):
    if i > 1000:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(
    tweets_list2, columns=["Datetime", "Tweet Id", "Text", "Username"]
)

tweets_df2.to_csv("tweets.csv", encoding="utf-8")
