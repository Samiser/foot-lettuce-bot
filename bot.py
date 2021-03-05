import tweepy
import number15
import json

def authenticate():
    with open('credentials.json', 'r') as c:
        creds = json.loads(c.read())
    
    auth = tweepy.OAuthHandler(
        creds['api_key'],
        creds['api_secret_key']
    )

    auth.set_access_token(
        creds['access_token'],
        creds['access_token_secret']
    )

    return tweepy.API(auth)

if __name__ == '__main__':
    api = authenticate()
    api.update_status(number15.generate())
