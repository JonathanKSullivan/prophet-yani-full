import tweepy
import os

class TwitterService:
    def __init__(self):
        consumer_key = os.environ.get('TWITTER_CONSUMER_KEY',  'XJMmFzlNfSUXrAMrqWQDJbY5j')
        consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET', 'nWXySYS5uXjUg6EBEWu5ppL7f3M7CVR6rhiUf3exRF1savNpEZ')
        access_token = os.environ.get('TWITTER_ACCESS_TOKEN', '1892602154-vNlOHdRPhLpFRVs2BnAWZZNawbiKl3cCeFafk1c')
        access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET', 'kmNUJoA9mf01Ln5l9MVy1KSdjlJRNBlxsWziM27MVKU3A')

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    @staticmethod
    def get_follower_count(username):
        try:
            user = self.api.get_user(screen_name=username)
            return user.followers_count
        except:
            return f"Tweepy Error"
