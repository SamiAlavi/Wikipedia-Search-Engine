import regex


## replaces every character except alphanumeric with space
## replaces \n character with space
def converter(soup):
    re = regex.compile("[^A-Za-z0-9\n]")
    fsoup = re.sub(" ", soup.text);
    fsoup = fsoup.replace("\n"," ")
    return fsoup

## returns list of words in title
## removes title from file
def getTitle(soup):
    titleList = []
    tList = []
    for t in soup.find_all('title'):
        s = converter(t)
        tList = s.split(" ")
        for t1 in tList:
            titleList.append(t1.strip().lower())
        t.decompose()
    return titleList

## removes script,style,link,title tags (if any) from file
def sanitize(soup):
    blacklist = ["script", "style","link","title"]
    for t in soup.find_all(blacklist):
        t.decompose()
    return soup

## returns list of words in headers
## removes headers from file
def getHeaders(soup):
    headList = []
    hList = []
    for t in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5']):
        s = converter(t)
        hList = s.split(" ")
        for header in hList:
            headList.append(header.strip().lower())    
        t.decompose()
    return headList,soup

## returns list of bold,underline,italic in file
## removes this list from file
def getBUI(soup):
    BUIList = []
    s = ""
    whitelist = ["b","u","i"]
    for t in soup.find_all(whitelist):
        s = t.text
        t.decompose()
        BUIList.append(s.strip().lower())
    return BUIList,soup


## returns list of all the words in the file
def getWords(soup):
    wordsList = []
    wList = []
    s = converter(soup)
    wList = s.split(" ")
    for word in wList:
        if word!='':
            wordsList.append(word.lower())
    return wordsList
