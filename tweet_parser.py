#!/usr/bin/env python

"""
Uses Twython to search through tweets by @dumpmon to determine if certain information shows up in information dumps
"""

import sys
import string
import simplejson
import urllib2
import smtplib
import time
import datetime
from info import *
from twython import TwythonStreamer

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            message = data['text'].encode('utf-8')
	    split_message = message.split()
	    response = urllib2.urlopen(split_message[0])
	    html = response.read()
	    time = datetime.datetime.now()
	    timeofday = time.time()
	    day = int(time.day)
	    month = int(time.month)
	    year = int(time.year)
	    found_info = "file_%i_%i_%i_%s.txt" % (month, day, year,timeofday)
	    fp = open(found_info, "w")
	    for substring in substrings:
		print substring
		if substring in html:
		   fp.write(html);
	    	   fp.close()
		   msg = "\r\n".join([
		        "From: %s" % fromaddr,
		        "To: %s" % toaddrs,
		        "Subject: Just a message",
		        "",
		        "This email: " + substring + " was found on " + time.strftime("%c") + " at " + split_message[0]
		        ])
		    server = smtplib.SMTP('smtp.gmail.com:587')
		    server.ehlo()
		    server.starttls()
		    server.login(username,password)
		    server.sendmail(fromaddr, toaddrs, msg)
		    server.quit()
	    print message 
    def on_error(self, status_code, data):
        print status_code

stream = MyStreamer(app_key=key, app_secret=secret_key, oauth_token=token, oauth_token_secret=token_secret)

stream.statuses.filter(follow="1231625892")
