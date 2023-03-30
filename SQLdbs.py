import sqlite3

## creates database
def createDatabase():
    conn = sqlite3.connect('Google2.db')

    conn.execute('''
    CREATE TABLE WORDS
    (URL VARCHAR(250),
    WORD VARCHAR(45));
    ''')

    conn.execute('''
    CREATE TABLE WORDDIST
    (WORD VARCHAR(45),
    URL VARCHAR(250),
    PAGERANK INT NOT NULL,
    IND INT NOT NULL);
    ''')             

    print ("Table created successfully")
    return conn


## drops database
def dropDatabase():    
    conn = sqlite3.connect('Google2.db')
    
    conn.execute('''
    DROP TABLE WORDS;''')
    
    conn.execute('''
    DROP TABLE WORDDIST;''')

    conn.commit()    
    conn.close()
    
def insertValues(fileName,wordsList):
    conn = sqlite3.connect('Google2.db')  
                     
    for word in wordsList:
        conn.execute('''INSERT INTO WORDS (URL, WORD) VALUES(?,?)''',(fileName, word)) ## docID, word

     
    conn.commit()
    conn.close()
    

## sorts the invertedIndexDict by key in ascending order
## prints the sorted invertedIndexDict dictionary
def insertSortedInvertedList(invertedIndexDict):
    conn = sqlite3.connect('Google2.db')
    
    for key in sorted(invertedIndexDict):
#        print (("%s: ") % (key))
        for i in invertedIndexDict[key]:
#           print (("%s: %s") % (key,i))            
            for j in i:
                if j=='index':
#                    print (("(%s:)(DOCID: %s) (FREQ: %s) (INDEX LIST: %s)") % (key,docID,p,invertedIndexDict[key][0].get('index')))
                    for w in invertedIndexDict[key][0].get('index'):
#                        print (("(%s:)(DOCID: %s) (FREQ: %s) (INDEX: %s)") % (key,docID,p,w))
                        conn.execute('''INSERT INTO WORDDIST (WORD, URL, PAGERANK, IND) VALUES(?,?,?,?)''', (key, docID, p, w))                      
                else:
                    docID = j
                    p = i.get(j)
    
    conn.commit()
    conn.close()
