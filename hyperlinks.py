import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
import re
import json
import sys
import json

total = 0
list_url = []
dump_file =''
HOME_DIR = ''
def obtain_json():
    global dump_file, HOME_DIR
    HOME_DIR = '/home/hugh/'
    count=0

    max_limit = 100
    initial_url = "http://www.zhihu.com/"  

    populate_list(initial_url)

    while len(list_url) < max_limit:
      populate_list(list_url[count])
      count += 1

    proto, rest = urllib.splittype(initial_url)
    res, rest = urllib.splithost(rest)
    if res:
      dump_file = res
    else:
      dump_file = 'urls.txt'  
    f1 = open(HOME_DIR + dump_file, 'w')        
    for element in list_url:  
      f1.write(element)
      f1.write('\n')
    f1.close()               

def populate_list(url):
    
    try:    
    
      global list_url
    
      page = urllib2.urlopen(url)
      soup = BeautifulSoup(page)

      for incident in soup.findAll('a',{'href': True}):
        try:
           if 'http' in str(incident['href']).encode('ascii','ignore'):
              list_url.append(str(incident['href']))
        except UnicodeEncodeError:
               print ''
    except:
        print ''  

def main():
    
    global list_url

    obtain_json()

def login(url, data):
    req = urllib2.Request(url)
    data = urllib.urlencode(data)
    #enable cookie
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    response = opener.open(req, data).read()
    
if __name__ == '__main__':
  posturl = "http://www.zhihu.com/"
  data = { 'username':'', 'password':'' }
  login(posturl, data)
  main()
