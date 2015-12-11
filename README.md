# Tweet-Parser

This is meant to take in a stream of tweets from the twitter bot @dumpmon  
It then goes to the pastebin, or other link and searches through the paste for supplied information  
This can be used to check if your credentials have been compromised, so that you can change them  
If it finds the the supplied information in the paste, it then will send an alert email to you as well as save the contents of the paste so that you can check your yourself  
For this to work, you have to supply the following information, in a file called info.py  

#Information to provide
substrings = ['email@email.com', 'Other string to find']  
key ='twitter consumer key here'  
secret_key ='twitter secret consumer key'  
token ='twitter access token'  
token_secret ='twitter secret access token'  
fromaddr = 'email to send from'  
toaddrs  = 'email to send to'  
username = 'email to send from'  
password = 'password of the from email'  

#Note
This was a simple program to test an idea, and is not meant to be used for anything other than an experiment  
You can also change the "stream.statuses.filter(follow="1231625892")" to have it follow any twitter account you would like, just change the follow value.
