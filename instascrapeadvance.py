from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
from openpyxl import load_workbook
import pandas as pd
import re
import csv
import os
path=os.path.join(os.getcwd(),"profile_bio.xlsx")
nameofperson=[]
username=[]
bioofperson=[]
urll=[]

# filter out all the wastefull words
def check(info):
    regex=re.compile(r'\\ud[\w]+')
    emoji=regex.findall(info)
    d=info
    for i in emoji:
        d=d.replace(i,'')
    d=d.replace("\\n",'')
    d=d.replace("\\",'')
    return d

external_sites_html =uReq("https://www.instagram.com/m.qasim077/")
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
urll.append(urlll[linkstart:linkend])
print("THIS is url :",urll[0])

#code for username
usernamestart=linkstart+26
usernameend=linkend-1
username.append(check(urlll[usernamestart:usernameend]))
print("This is username:",username[0])
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

nameofperson.append(check(name()))
print("this is name:",nameofperson[0])
bioofperson.append(check(bio()))
print("THIS is Person's Bio is:",bioofperson[0])





df=pd.DataFrame({
    "Name" : nameofperson,
    "User Name": username,
    "urls" :urll,
    "Bio" : bioofperson
})
try:
    writer = pd.ExcelWriter(path, engine='openpyxl')
    # try to open an existing workbook
    writer.book = load_workbook(path)
    # copy existing sheets
    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
    # read existing file
    reader = pd.read_excel(f"{path}")
    # write out the new sheet
    df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)
    print('Spreadsheet saved.')
    writer.close()

except:
    df.to_excel(os.path.join(path), index=False)
    print('Spreadsheet saved.')
