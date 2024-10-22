# _Twitter-Sentiment-Analysis_

### _This project is a Twitter Sentiment Analysis web application built using Flask for the backend, Tweepy for accessing the Twitter API, and TextBlob for sentiment analysis. Here’s a summary of the functionality_

### _**Tweet Cleaning:**_ 

The clean_tweet function removes mentions, special characters, and URLs from tweets to prepare them for sentiment analysis.

### _**Sentiment Analysis:**_

The get_tweet_sentiment function analyzes a tweet's sentiment using TextBlob based on polarity, classifying tweets as "positive", "neutral", or "negative".
There’s an option (commented out) to use NaiveBayesAnalyzer for more detailed sentiment classification.

### _**Fetching Tweets:**_

The get_tweets function fetches a specified number of tweets using Tweepy’s API based on a user-defined query, and analyzes each tweet’s sentiment.

### _**Flask Routes:**_

Home Route (/):Displays the main interface with two options for sentiment analysis.
Phrase-Level Sentiment Analysis (/predict): Fetches and analyzes multiple tweets based on a query.
Sentence-Level Sentiment Analysis (/predict1): Analyzes the sentiment of a single user-provided sentence.

### _**Front-End:**_ 

The app uses Bootstrap for a responsive layout and includes two forms:

One for phrase-level sentiment analysis (tweet fetching).
One for sentence-level sentiment analysis (user input).
