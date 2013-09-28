import os
import urllib
import urllib2

global key
key = os.getenv('SEMRUSH_KEY')


def keyword_competition(keyword):
    args = {
        'action': 'report',
        'type': 'phrase_this',
        'key': key,
        'export': 'api',
        'export_columns': 'Ph,Nq,Cp,Co,Nr',
        'phrase': keyword
    }

    return semrush(args)


def domain_traffic(domain):
    args = {
        'action': 'report',
        'type': 'domain_rank',
        'key': key,
        'display_limit': '20',
        'export': 'api',
        'export_columns': 'Dn,Rk,Or,Ot,Oc,Ad,At,Ac',
        'domain': domain
    }

    return semrush(args)


def keyword_organic(keyword):
    args = {
        'action': 'report',
        'type': 'phrase_organic',
        'key': key,
        'display_limit': '20',
        'export': 'api',
        'export_columns': 'Dn,Ur',
        'phrase': keyword
    }

    return semrush(args)


def semrush(args):
    base_url = 'http://us.api.semrush.com/'
    arg_string = urllib.urlencode(args)
    url = base_url + "?" + arg_string

    response = urllib2.urlopen(url)
    data = response.read()
    response.close()

    for i, line in list(enumerate(data.split('\n')))[1:]:
        line = line.strip()
        fields = line.split(';')

        yield i, fields
