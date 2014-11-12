# coding: utf-8
import os
import urllib2
import twitter
import sys


def check_in():
    ''' Check at 5am everyday or after reboot if dev server IP changed - if so,
    send me a twitter direct message'''
    IP = open("current_ip_address.txt", 'r')
    for line in IP:
        address = line.strip()
    IP.close()
    fqn = os.uname()[1]
    ext_ip = urllib2.urlopen('http://bot.whatismyipaddress.com').read().strip()
    print ("Asset: %s " % fqn, "Checking in from IP#: %s " % ext_ip)
    match = address == ext_ip
    if not match:
        api = twitter.Api(consumer_key='hVEthMMjJkXSzeRU71tDS8WTy',
                          consumer_secret='B6jOFoHTerQzXjvZPRHPtlGCfKNmKPRx18KKQQhYPLl4bQrXEJ',
                          access_token_key='7060462-3TWE0lFBR3JURIMf0Zs74ndu4EOJBSRNX9gk7NGe3V',
                          access_token_secret='Tzp60433O1B8UUyYo3O3kN6cp83dNqIxi98ot1Vrzy3yJ')
        api.PostDirectMessage(screen_name='larrygray', text='Your IP Address has changed to {0}'.format(ext_ip))
        with open("current_ip_address.txt", 'w') as new_ip:
            new_ip.write(ext_ip)

if '__main__' == __name__:
    sys.exit(check_in())
