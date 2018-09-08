#!/usr/bin/python
# encoding=utf8
from datetime import datetime
from pywinauto import application, Application, Desktop
import pywinauto.mouse 
from pywinauto.keyboard import SendKeys
import win32api
import time
import urllib2
from bs4 import BeautifulSoup
import requests

urlOne = "https://www.google.com.co/search?biw=1280&bih=635&ei=TQAsWseaJcrXmAHQ273YBg&q=az+seguros&oq=az+seguros&gs_l=psy-ab.3...665612.668298.0.668411.0.0.0.0.0.0.0.0..0.0....0...1.1.64.psy-ab..0.0.0....0._Qs4s56HkxM"
urlD = "https://web.azseguros.com/main/"
#url = 'https://www.google.com.co/search?q=az+seguros&oq=az+s&aqs=chrome.0.69i59j69i57j69i60l3j0.832j0j7&sourceid=chrome&ie=UTF-8'
chrome = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
app = Application(backend='uia')
#app.start(chrome + ' --force-renderer-accessibility --start-maximized ' + url)
#headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = urllib2.urlopen(urlD)
#response = requests.get(urlOne, headers=headers)
#print(response.content)
soup = BeautifulSoup(page, "html.parser")
searcher = "title"
title = soup.find_all(searcher)
title = str(title)
title = title.replace("<" + searcher + ">","")
title = title.replace("</" + searcher + ">", "")
print(title)

#print(app.print_control_identifiers())


path = "C:\\Users\\feli2\\Documents\\Cali.txt"


f = open(path, 'r')
f = f.read()
f = f.split('\n')

#print(str(f) + "FUCK")

for i in f:
    
    objOne = (i).split(' ')
    print(str(objOne) + "YES")
    objOne = BeautifulSoup(str(objOne),"html.parser")
    app.start(chrome + ' --force-renderer-accessibility --start-maximized ' + "https://www.google.com")
    
    time.sleep(1)
    
    SendKeys('{F6}' + str(objOne))
    SendKeys('{ENTER}')

    
    '''for j in objOne:

        out = j.split('\n')

        #print(str(out) + "NO")

        for x in out: 
            #x = x.replace('[edit]', ' ')
            #x = x.replace(';', ' ')
            #out = (out.replace('&ndash',' '))
            
            x = (x.split('\\'))

            #print(str(x) + "YES")
            
            ''''''app.start(chrome + ' --force-renderer-accessibility --start-maximized ' + "https://www.google.com")

            time.sleep(1)

            SendKeys('{F6}' + str(x))

            SendKeys('{ENTER}')
            
            print(x)
           
            app.start(chrome + ' --force-renderer-accessibility --start-maximized ' + "https://www.google.com")
            time.sleep(1)
            SendKeys('{F6}' + (x))
            
'''
