'''Quick Script to monitor IP Address Changes'''
# coding: utf-8
import os
import urllib2
import twitter
import sys


def check_in():
    ''' Check at 5am everyday or after reboot if dev server IP changed - if so,
    send me a twitter direct message'''
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    access_token_key = os.getenv('access_token_key')
    access_token_secret = os.getenv('access_token_secret')
    ip_address = open("current_ip_address.txt", 'r')
    for line in ip_address:
        address = line.strip()
    ip_address.close()
    fqn = os.uname()[1]
    ext_ip = urllib2.urlopen('http://bot.whatismyipaddress.com').read().strip()
    print ("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip)
    match = address == ext_ip
    if not match:
        api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret,
                          access_token_key=access_token_key,
                          access_token_secret=access_token_secret)
        api.PostDirectMessage(screen_name='larrygray',
                              text='IP Address changed to {0}'.format(ext_ip))
        with open("current_ip_address.txt", 'w') as new_ip:
            new_ip.write(ext_ip)

if '__main__' == __name__:
    sys.exit(check_in())
