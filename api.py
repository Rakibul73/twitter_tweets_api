from datetime import datetime
import json
import eda_key

from flask import Flask, jsonify
import tweepy

app = Flask(__name__)
@app.route('/latest_tweet/<username>')
def latest_tweet(username):
    # Authenticate to Twitter API
    auth = tweepy.OAuthHandler(eda_key.YOUR_CONSUMER_KEY, eda_key.YOUR_CONSUMER_SECRET)
    auth.set_access_token(eda_key.YOUR_ACCESS_TOKEN, eda_key.YOUR_ACCESS_SECRET)

    # Create API object
    api = tweepy.API(auth)

    # Get the latest tweet from a user
    tweet = api.user_timeline(screen_name=username, count=1, tweet_mode="extended")[0]
    
    

    # Format tweet data and return as JSON
    tweet_data = {
        "text": tweet.full_text,
        "timestamp": datetime.strftime(tweet.created_at, "%Y-%m-%d %H:%M:%S"),
        "username": tweet.author.name,
    }
    return jsonify(tweet_data)

if __name__ == '__main__':
    app.run(debug=True)
