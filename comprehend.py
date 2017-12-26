import boto3

client = boto3.client('comprehend')
s3 = boto3.resource('s3')

obj = s3.Object('twitter-feed-mt', 'twitter-status2017/12/20/17/twitter-s3-1-2017-12-20-17-50-06-82960183-6c8d-40c6-a8aa-448d70052f9e copy.txt')
tweet = obj.get()['Body'].read().decode('utf-8')

feeling = client.detect_sentiment(Text=tweet, LanguageCode='en')
convo = client.detect_key_phrases(Text=tweet, LanguageCode='en')
print (feeling)
print (convo)
