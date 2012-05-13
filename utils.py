absolutize = lambda l: ('http://pravda.com.ua%s' % l) if l.startswith('/') else l

def make_absolute_url():
    for p in Post.objects:
        p.links = [absolutize(link) for link in p.links]
        p.save()

#########

from collections import Counter
from urlparse import urlparse
import re

www = re.compile(r'^www\.')

def count_links():
    c = Counter()
    for post in Post.objects:
        for link in post.links:
            parsed = urlparse(link)
            hostname = str(parsed.hostname)
            c[re.sub(www, '', hostname)] += 1
    return c

#########

fixer = lambda l: l.replace('http://pravda.com/ua', 'http://pravda.com.ua')

def fix_pravda_url():
    for post in Post.objects:
        p.links = [fixer(l) for l in p.links]
        p.save()

##########

domains = [
    r'^www',
    r'\.com(/W|$)',
    r'\.ua$',
    r'\.ru$',
    r'\.kiev',
    r'\.gov',
    r'\.kharkov',
    r'\.net',

]

def get_source(hostname):

