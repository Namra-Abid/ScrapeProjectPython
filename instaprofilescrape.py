from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd
import re
import csv

external_sites_html =uReq("https://www.instagram.com/")
soup = BeautifulSoup(external_sites_html, 'lxml')
detail_list=soup.find("script",{"type":"application/ld+json"})
ss=detail_list.prettify()

#---code for URL---
des=soup.find('meta', attrs={'property':'og:url'})
urlll=des.prettify()
desc = re.search(r'\b(property)\b', urlll)
gd=desc.start()
linkend=gd-2
print("ENDING",linkend)
link = re.search(r'\b(https)\b', urlll)
linkstart=link.start()
print("START",linkstart)
urll=urlll[linkstart:linkend]
print("THIS is url :",urll)
#code for username
usernamestart=linkstart+26
usernameend=linkend-1
username=urlll[usernamestart:usernameend]
print("This is username:",username)
#PERSON name
person=re.search(r'\b(name)\b',ss)
namestart=person.start()+7
def name():
    personend=re.search(r'\b(alternateName)\b',ss)
    if personend!=None:
        nameend=personend.start()-3
        prname=ss[namestart:nameend]
        #print("This is name :",prname)
        return prname
    else:
        personend=re.search(r'\b(description)\b',ss)
        nameend=personend.start()-3
        prname=ss[namestart:nameend]
        #print("This is name :",prname)
        return prname



def bio():
    searchfor=re.search(r'\b(mainEntityofPage)\b',ss)
    personbio=re.search(r'\b(description)\b',ss)
    if personbio != None:
        biostart=personbio.start()+14
        bioend=searchfor.start()-3
        bio=ss[biostart:bioend]
        return bio
    else:
        bio="N/A"
        return bio

nameofperson=name()
print("this is name:",nameofperson)
bioofperson=bio()
print("THIS is Person's Bio is:",bioofperson)

with open("data2.csv","a") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow([nameofperson,username,urll,bioofperson])
    csvfile.close()
