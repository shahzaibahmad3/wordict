from urllib.request import urlopen
from bs4 import BeautifulSoup

def getmean(word):
    url = "https://www.merriam-webster.com/dictionary/"+word
    
    htmlfile=""
    try:
        htmlfile = urlopen(url)
        html = htmlfile.read()
        
        html = html.decode('utf-8')
        
        start_content = html.find('data-share-description')
        html = html[start_content+24:]
        end_content = html.find("See the full definition")
        
        content = html[:end_content]
        
        meanings = content.split(";")
        meanings
        means="meaning: \n"
        
        i=1
        for mean in meanings:
            means=means+""+mean+"\n\n"
            i=i+1
        
        return means
    except:
        return "check spelling"

print(getmean("cat"))
