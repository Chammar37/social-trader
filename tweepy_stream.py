import tweepy

class MyListener(StreamListener):
        def on_data(self, data):
            print(data)
            return True

listener = MyListener()
auth = OAuthHandler(E6EnVEln9E4XubkgUNec5S87p, Soo0CC2gusNpBJiE5SXXGcawclZC9hXWgY5LWDGze6KvNHBh9m)
auth.set_access_token(1032147310304808961-DYpRYrehYu3o7bw4r1kvKRZ9HKxPHU, EE3sJuZ1dBG9L9q8dzxAuD5Zv1sLOMNgDJxlc58u04DD6)
stream = Stream(auth, listener)
stream.filter(follow=['714640046888984577'])  # assume this user is a celebrity