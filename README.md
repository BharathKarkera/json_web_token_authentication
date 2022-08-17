# json_web_token_authentication


*Get the current time stamp in unix timestamp in seconds:*

>>> print(datetime.datetime.utcnow())
2022-08-16 22:34:16.852410


*Generate 30 seconds of time delta :*


>>> print(datetime.timedelta(seconds=30))
0:00:30
>>> 


*When we add both together , we will set this as token expiry time which means token will expire after 30 seconds at : 2022-08-16 22:34:46.397718*

>>> print(datetime.datetime.utcnow() + datetime.timedelta(seconds=30))
2022-08-16 22:34:46.397718
>>> 


*Generating tokens using JWT :*

>>> print(jwt.encode({'user':'bharath' , 'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=30)} ,'my_secret_key' ))
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYmhhcmF0aCIsImV4cCI6MTY2MDY5ODUzNX0.UrHWYRWZ6D0vFxTwC333uuwDm2QjHDfHxUFEI-_rrVc
>>> 
>>> 
>>> print(jwt.decode("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYmhhcmF0aCIsImV4cCI6MTY2MDY5ODUzNX0.UrHWYRWZ6D0vFxTwC333uuwDm2QjHDfHxUFEI-_rrVc", "my_secret_key", algorithms=['HS256']))
{'user': 'bharath', 'exp': 1660698535}
>>> 

