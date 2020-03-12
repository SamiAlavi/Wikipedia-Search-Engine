import sqlite3

def searchMultiWords(wordList):
    times=0
    
    conn=sqlite3.connect('Google2.db')
    
    cur = conn.cursor()

    sqlquery=""

    url=[]
    args=[]
    freq=[]

    for i in wordList:
        args.append(i)
        sqlquery+= " UNION SELECT DISTINCT URL,PAGERANK FROM WORDDIST WHERE WORD=?"
    sqlquery+= " ORDER BY PAGERANK DESC"
    
    cur.execute(sqlquery[6:],args)

    rows = cur.fetchall()
    
    for row in rows:
        if row[0] not in url:
            url.append(row[0])
            freq.append(row[1])
        else:
            index=url.index(row[0])
            freq[index]+=20  
        
    for i in url:                
        index=url.index(i)
        for j in wordList:
            if j.title() in i:
                freq[index]+=5

    sortedURLs = [x for _,x in sorted(zip(freq,url),reverse=True)]
    
    return sortedURLs,freq,url       
