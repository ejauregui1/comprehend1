## Comprehend1
#### CodeName: 'Buba-licious'
The 'Buba-licious' project was born during the 2017 (mt) Media Temple Winter Hackathon. The idea was to use AWS Comprehend to take public information from social media and obtain content sentiment.

#####The WorkFlow being accomplished with Python & AWS

→  twitter_kinesis.py  (source → data streams)

→  kinesis (data stream → analytics sql query →  firehose → S3)

→  comprehend_firehose.py Script (S3 file → py → data firehose → es)

→  Kibana
