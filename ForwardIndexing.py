import requests
from lxml import html
from bs4 import BeautifulSoup
from IndexingHelper import sanitize,getTitle,getHeaders,getBUI,getWords


## html parser
def storeDetails(path):
    f = open(path, encoding='latin-1')
    soup = BeautifulSoup(f, "html.parser")

    titleList=getTitle(soup) ## see IndexingHelper file
    
    soupS=sanitize(soup) ## see IndexingHelper file

    headers,soupMH=getHeaders(soupS) ## see IndexingHelper file
    BUIList,soupMBUI=getBUI(soupMH) ## see IndexingHelper file
    wordsList=getWords(soupMBUI) ## see IndexingHelper file
   

    return titleList,headers,BUIList,wordsList; ## returns dictionaries








