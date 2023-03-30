
## adds word as key in invertedIndexDict dictionary
## this key has value of list
## the  list contains sub-dictionaries
## sub-dictionary contains URL as key and its PAGERANK as value
def invertedIndex(URL, invertedIndexDict, unique, pageRank, wordsList):
    
    for i in range(len(unique)):
        indexes=[index for index, value in enumerate(unique) if value == unique[i]]
        
        if unique[i] in invertedIndexDict:
            invertedIndexDict[unique[i]].append({URL:pageRank[i],'index':indexes})
        else:
            invertedIndexDict[unique[i]] = [{URL:pageRank[i],'index':indexes}]
    


