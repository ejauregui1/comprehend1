## Comprehend1
### CodeName: 'Buba-licious'
The 'Buba-licious' project was born during the 2017 (mt) Media Temple Winter Hackathon. The idea was to use AWS Comprehend to take public information from social media and obtain content sentiment.

#### The WorkFlow being accomplished with Python & AWS

→  twitter_kinesis.py  (source → data streams)

→  kinesis (data stream → analytics sql query →  firehose → S3)

→  comprehend_firehose.py Script (S3 file → py → data firehose → es)

→  Kibana


#### What was the goal of this idea?
Since this was a part of a 3 day project I committed to using Twitter as my main source. The idea is that we can build better data using other forms of social media that allow for rest api access and/or access to data. (ie: linkedIn, Google Alerts, Facebook, etc. )


### API information

#### LinkedIn API
Python Notes
- Install linked in python package
- `pip install python-linkedin`
- If using Python 3 you will receive an error and will need to update with the following package.
- ` pip install --upgrade https://github.com/ozgur/python-linkedin/tarball/master`
