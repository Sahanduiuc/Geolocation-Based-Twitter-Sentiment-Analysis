from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentimentDetectionModule as s


#consumer key, consumer secret, access token, access secret.
consumer_key ="Consumer_Key"
consumer_secret="Consumer_Secret"
access_token="Access_Token"
access_token_secret="Access_Token_Secret"

class listen_data(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        try:
            tweet = all_data['text']
            sentiment, confidence = s.sentiment(tweet.lower())
            print(tweet, sentiment, confidence)
            if confidence*100 >= 75:
                output_file = open('Tweet_Sentiments.txt','a')
                output_file.write(sentiment)
                output_file.write('\n')
                output_file.close()
            return True
        except:
            return True
    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

twitter_data_stream = Stream(auth,listen_data())
twitter_data_stream.filter(track=['Donald Trump'],locations=[-122.75,36.8,-121.75,37.8])
