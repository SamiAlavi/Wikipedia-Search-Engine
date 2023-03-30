import os
from ForwardIndexing import storeDetails
from InvertedIndexing import invertedIndex
from SQLdbs import createDatabase,dropDatabase,insertValues,insertSortedInvertedList
import time

start = time.time()
#dropDatabase()
conn = createDatabase()

count = 0  ## documentID
limit = 10000 ## number of files to parse

invertedIndexDict = dict()

parent = 'D:/1Wikipedia/simple/articles/' ## parent directory for articles

## 3 loops for going through each .html page in parent directory
for alph_one in os.listdir(parent):
    if count==limit:
            break
    for alph_two in os.listdir(parent+alph_one+"/"):
        if count==limit:
            break
        for alph_three in os.listdir(parent+alph_one+"/"+alph_two+"/"):
            if count==limit:
                break
            for filename in os.listdir(parent+alph_one+"/"+alph_two+"/"+alph_three+"/"):
                
                if count==limit:
                    break
                if count%1000==0:
                    print(count)
                    print("Seconds for "+str(count)+" articles: "+str(time.time() - start))
                    print()
                    
                if filename.endswith('.html'):
                    fileName = os.path.join(parent+alph_one+"/"+alph_two+"/"+alph_three+"/",filename)
                    count+=1
                    
                    titleList, headings, BUIList, wordsList = storeDetails(fileName) ## see ForwardIndexing file
                    
                    unique = []   ## unique words
                    pageRank = []     ## pageRank of unique words

                    ## create both arrays for every .html file
                    for word in wordsList:
                        if word not in unique:
                            unique.append(word)
                            pageRank.append(1)                       
                        else:
                            i = unique.index(word)
                            pageRank[i]+= 1
                            
                    for title in titleList:
                        if title not in unique:
                            unique.append(title)
                            pageRank.append(100)                       
                        else:
                            i = unique.index(title)
                            pageRank[i]+= 100

                    for heading in headings:
                        if heading not in unique:
                            unique.append(heading)
                            pageRank.append(3)                       
                        else:
                            i = unique.index(heading)
                            pageRank[i]+= 3

                    for bui in BUIList:
                        if bui not in unique:
                            unique.append(bui)
                            pageRank.append(2)                       
                        else:
                            i = unique.index(heading)
                            pageRank[i]+= 2
                            
                    #insertValues(fileName,wordsList) ## see SQLdbs file                                                 (FORWARD INDEX)
                            
                    invertedIndex(fileName, invertedIndexDict, unique, pageRank, wordsList) ## see InvertedIndexing file    (REVERSE INDEX)

#print(invertedIndexDict)
                    
insertSortedInvertedList(invertedIndexDict) ## see SQLdbs file       

tt = time.time() - start
print()
print("Total  Time Taken:")
print("Seconds for "+str(count)+" articles: "+str(tt))
print("Minutes for "+str(count)+" articles: "+str(tt/60))
print("Hours for "+str(count)+" articles: "+str(tt/3600))
