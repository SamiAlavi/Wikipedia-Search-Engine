import sqlite3
import time
from singleword import searchSingleWord
from multiword import searchMultiWords

def check(wordList):
    #if only single word, use real pageRank, see searcher.py
    #if multi word, use modified pageRank, see mws.py

    if (len(wordList)==1):
        start = time.time()
        results, freq = searchSingleWord(wordList[0])        
        duration = time.time() - start        
        return results, duration
    else:
        start = time.time()        
        sortedURLs, freq, url = searchMultiWords(wordList)        
        duration = time.time() - start        
        return sortedURLs, duration
