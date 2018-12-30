import sqlite3
import time
##import regex
from singleword import searchSingleWord
from multiword import searchMultiWords     

##def converter(query):
##    re=regex.compile("[^a-z0-9]")
##    query=re.sub(" ",query);
##    return query

def printMultiWordResults(urlList):
    for i in range(len(urlList)):
        if i==10:
            break;
        print(urlList[i])

def printSingleWordResults(urlList):
    for i in range(len(urlList)):
        if i==10:
            break;
        print(urlList[i])

###enter word here
##query=input("Enter word to search: ").lower().strip()
##
###replace non-alphanumeric with space and make a list
##query=converter(query)    
##wordList=query.split()

def check(wordList):
    #if only single word, use real pageRank             see searcher.py
    #if multi word, use modified pageRank               see mws.py
    if len(wordList)==1:
        start=time.time()
        
        results,freq=searchSingleWord(wordList[0])
        
        duration=time.time()-start
        
        return results,duration
    
        printSingleWordResults(results)
    else:
        start=time.time()
        
        sortedURLs,freq,url=searchMultiWords(wordList)
        
        duration=time.time()-start
        
        return sortedURLs,duration
    
        printMultiWordResults(sortedURLs)


##start=time.time()
##tt=time.time()-start
##print()
##print("words: ",wordList)
