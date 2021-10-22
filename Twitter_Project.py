import tweepy
from tweepy import StreamListener
import re
from tweepy_credentials import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Getting Stream
class MaxListener(StreamListener):
    def on_status(self, status):
        if (status.user.id_str == '714640046888984577'):
            if ('$' in status.text):
                ticker = re.findall(r'[$][A-Za-z][\S]*', str(status.text))
                ticker = ticker[0].replace('$', '')
                return print(ticker)

    def on_error(self, status_code):
        if status_code == 420:
            return False

# Keys from Twitter
# API_KEY = 'E6EnVEln9E4XubkgUNec5S87p'
# API_SECRET_KEY = 'Soo0CC2gusNpBJiE5SXXGcawclZC9hXWgY5LWDGze6KvNHBh9m'
# ACCESS_TOKEN = '1032147310304808961-DYpRYrehYu3o7bw4r1kvKRZ9HKxPHU'
# ACCESS_TOKEN_SECRET = 'EE3sJuZ1dBG9L9q8dzxAuD5Zv1sLOMNgDJxlc58u04DD6'

# Starting Stream


class MaxStream():
    def __init__(self, auth, listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self):
        # follow=['714640046888984577']
        return self.stream.filter( follow=['714640046888984577'])


# Main method
if __name__ == "__main__":
    auth = tweepy.OAuthHandler(API_KEY,
                               API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN,
                          ACCESS_TOKEN_SECRET)

    listener = MaxListener()

    stream = MaxStream(auth, listener)
    stream.start()
    print("moving to on status")
