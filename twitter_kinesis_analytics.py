## Example to use twitter api and feed data into kinesis

from twitter import (Twitter, OAuth)
from settings import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, TWITTER_USER_LIST)
import pprint
import boto3
import json
import sys

t = Twitter(auth=OAuth(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

kinesis = boto3.client('kinesis')

for user in TWITTER_USER_LIST:
    r = t.statuses.user_timeline(screen_name=user)
    for item in r:
        try:
            kinesis.put_record(StreamName="twitter_analytics", Data=json.dumps(item), PartitionKey="filler")
        except:
            pass
