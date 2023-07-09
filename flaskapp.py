

import traceback
from flask import Flask, render_template
import requests
import xml.etree.ElementTree as eltree

APP=Flask(__name__)

@APP.route('/')

def UN_xml_Fetch():
  try:
  
  
   response=requests.get('https://news.un.org/feed/subscribe/en/news/all/rss.xml')
   print(response.content)
   
   root=eltree.fromstring(response.content)
   
   data=[]
   
   for item in root.findall('channel/item'):
     
     title=item.find('title').text
     print(title)
     data.append(title)
     
   return render_template('index.html',data=data)  
 
 
 
  except Exception as exc:
    traceback.print_exc()
    return "XML FETCH ERROR"
  
  
  
  
if __name__=='__main__':
    APP.debug=True
    APP.run()
    
      