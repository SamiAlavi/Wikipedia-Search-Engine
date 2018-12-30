import sqlite3
import time

def searchSingleWord(word):
    url=[]
    freq=[]
    times=0
    conn=sqlite3.connect('Google2.db')
    
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT URL,PAGERANK FROM WORDDIST WHERE WORD=? ORDER BY PAGERANK DESC",(word,))
    
    rows = cur.fetchall()

    for row in rows:
        url.append(row[0])
        freq.append(row[1])
        times+=1
        if times==10:
            break;
        
    return url,freq    


##word=input("Enter word to search: ").lower()
##start=time.time()
##url=selectFile(word)
##for i in url:
##    print(i)
##tt=time.time()-start
##print()
##print("Seconds: ",tt)
