import re, time, os, shutil, HTMLParser

import requests

if os.path.exists('scraper_cache'):
  shutil.rmtree('scraper_cache')
os.mkdir('scraper_cache')

url = 'https://www.facebook.com/careers/jobs?page={}'
num_pulls = 1000
for i in range(1, num_pulls):
  print 'pulling page:', i
  html = requests.get(url.format(i)).content
  with open(os.path.join('scraper_cache/{}.html'.format(i)), 'w') as f:
    f.write(html)
  time.sleep(2)
