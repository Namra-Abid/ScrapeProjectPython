from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import pandas as pd
import re
import csv

external_sites_html =uReq("https://www.instagram.com/")
soup = BeautifulSoup(external_sites_html, 'lxml')
detail_list=soup.find("script",{"type":"application/ld+json"})
print(detail_list)
#---code for url---
des=soup.find('meta', attrs={'property':'og:url'})
urlll=des.prettify()
desc = re.search(r'\b(property)\b', urlll)
gd=desc.start()
gg=gd-2
print("ENDING",gg)
descq = re.search(r'\b(https)\b', urlll)
ggq=descq.start()
print("START",ggq)
urll=urlll[ggq:gg]
print(urlll[ggq:gg])
#---code for url--- end here

print("**************************")
# NAME HERE
description = soup.find('meta', attrs={'property':'og:description'})
desurl=description.prettify()
point = re.search(r'\b(from)\b', desurl)
pointS=point.start()
print(pointS)
pointN = re.search(r'\D(@)\D', desurl)
pointSN=pointN.start()
print(pointSN)
alternate=desurl[pointS+4:pointSN]
print(alternate)


print(desurl)


ss=detail_list.prettify()
q=type(ss)
print("TYPE",q)
desc = re.search(r'\b(description)\b', ss)
print("bio",desc.start())
descS=desc.start()
descSP=descS+14
#-----------------------
altname = re.search(r'\b(alternateName)\b', ss)
if altname !=None:
#p=altname.start()
#print("alt",altname.start())
    alS=altname.start()
    alSP=alS+16
    alEnd=descS-3
else:

    altname=re.search(r'\b(name)\b', ss)
    nameS=altname.start()
    alS=descS
    alSP=nameS+7
    alEnd=descS-3
#..................
ud= re.search(r'\b(mainEntityofPage)\b', ss)
print(ud.start())

udS=ud.start()-3

#-------------------
namee = re.search(r'\b(name)\b', ss)
print("name",namee.start())
nameS=namee.start()
nameSP=nameS+7
nameEnd=alS-3
#----------------
interactionStatistic=re.search(r'\b(interactionStatistic)\b', ss)
print("interactionStatistic",interactionStatistic.start())
interaction=interactionStatistic.start()
id = re.search(r'\b(ProfilePage)\b', ss)
print("url",id.start())
idS=id.start()
idSP=idS+20
idEnd=interaction-4






#print(ss['alternateName'])
#print(len(ss))
print(detail_list)
print("------------------------")
#url=ss[439:478]
url=ss[idSP:idEnd]
#nam=ss[96:106]
nam=ss[nameSP:nameEnd]
#alt=ss[125:135]
alt=ss[alSP:alEnd]
bio =ss[descSP:udS]
print("THIS IS URL",urll)
print("THIS IS ALTERNA",alternate)
print("this is is url :",url)
print("this is is username :",alt)
print("this is is name :",nam)
print("this is is bio :",bio)
print("------------------------")
#e=detail_list.get('name')
#print(e)


#e=detail_list.get('name')






# information about followers and following users


print("------------------------")
#e=detail_list.get('name')
print(detail_list)
print("------------------------")
#e=detail_list.get('name')
#print(ss)
w=len(detail_list)
print(w)


with open("data1.csv","a") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow([alt,nam,urll,bio])
    csvfile.close()
