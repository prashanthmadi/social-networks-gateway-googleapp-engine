import tweepy
from com.prashanth.constants import SocialConstants

def twLogin():
    auth = tweepy.OAuthHandler(SocialConstants.TWITTER_CONSUMER_KEY, SocialConstants.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(SocialConstants.TWITTER_ACCESS_TOKEN, SocialConstants.TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api.me().name
