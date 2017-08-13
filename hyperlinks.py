import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup
import re
import json
import sys
import json

total = 0
list_url=[]
dump_file=''

def obtain_json():

    count=0

    max_limit = 1000
    initial_url = "http://www.zhihu.com/"  

    populate_list(initial_url)

    while len(list_url) < max_limit:
      populate_list(list_url[count])
      count+=1
                     

def populate_list(url):
    
    try:    
    
      global list_url
      global dump_file
    

      page = urllib2.urlopen(url)
      soup = BeautifulSoup(page)

      for incident in soup.findAll('a',{'href': True}):
        try:
           if 'http' in str(incident['href']).encode('ascii','ignore'):
              list_url.append(str(incident['href']))
        except UnicodeEncodeError:
               print ''
 
      with open(dump_file, "w") as file:
        json.dump( {'url':url,'outgoing':list_url}, file, indent=4)
      file.close()

    except:
        print ''  



def read():

    with open(dump_file) as file:
       result = json.load(file)
    file.close()
    print (type(result))
    print (result.keys())
    print (result)
        


def main():
    
    global list_url
    global dump_file

    dump_file =    "/home/hugh/Desktop/axc.txt"

    obtain_json()
    read()

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
