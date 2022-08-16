# json_web_token_authentication


Get the current time stamp in unix timestamp in seconds:

>>> print(datetime.datetime.utcnow())
2022-08-16 22:34:16.852410


Generate 30 seconds of time delta :


>>> print(datetime.timedelta(seconds=30))
0:00:30
>>> 


When we add both together , we will set this as token expiry time which means token will expire after 30 seconds at : 2022-08-16 22:34:46.397718

>>> print(datetime.datetime.utcnow() + datetime.timedelta(seconds=30))
2022-08-16 22:34:50.397718
>>> 
