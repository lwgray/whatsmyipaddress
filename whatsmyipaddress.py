#! /usr/bin/env python
'''Quick Script to monitor IP Address Changes'''
import os
import urllib2
import twitter
import sys


def check_in():
    ''' Check at 5am everyday or after reboot if dev server IP changed - if so,
    send me a twitter direct message'''
    consumer_key = os.getenv('twitter_consumer_key')
    consumer_secret = os.getenv('twitter_consumer_secret')
    access_token_key = os.getenv('twitter_access_token_key')
    access_token_secret = os.getenv('twitter_access_token_secret')
    twitter_screen_name = os.getenv('twitter_screen_name')
    with open("current_ip_address.txt", 'r') as ip_address:
        for line in ip_address:
            address = line.strip()
    fqn = os.uname()[1]
    # Reteive IPv6 address
    ext_ip = urllib2.urlopen('http://bot.whatismyipaddress.com').read().strip()
    print("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip)
    # verify if IP address has changed
    # if changed --> tweet direct message new address
    # if not changed --> Do nothin
    match = address == ext_ip
    if not match:
        print("IP Address has changed --> Tweet Sent!")
        api = twitter.Api(consumer_key,
                          consumer_secret,
                          access_token_key,
                          access_token_secret)
        api.PostDirectMessage(screen_name=twitter_screen_name,
                              text='IP Address changed to {0}'.format(ext_ip))
        with open("current_ip_address.txt", 'w') as new_ip:
            new_ip.write(ext_ip)

if '__main__' == __name__:
    sys.exit(check_in())
