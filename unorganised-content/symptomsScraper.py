import urllib
import urllib2
from bs4 import BeautifulSoup

def isSymptom( x ):
    arr=""
    ans=""
    i,l=0,len(x)
    while i<l:
        if( (x[i]!=' ' and x[i]!='\n' and x[i]!='\t')):
            arr+=x[i]
        else:
            if(len(ans)!=0):
                ans+=" "
            ans+=arr
            arr=""
        i+=1
        if(i<l and x[i]>=65 and x[i]<=90):
            ans[len(ans)-1]='\n'
    print ans
    return ans

def scraper(myUrl):
    pageSrc=""
    #results = urllib.urlopen(myUrl)
    with open("symptomsCheckerSite.txt") as f1:
        pageSrc=f1.read()
    soup=BeautifulSoup(pageSrc)
    with open("symptomsList.txt","w") as f:
        for x in soup.find_all('div','landing_views'):
            for y in x.find_all('div','content','content2'):
                for z in y.find_all('div','list'): 
                    t=z.get_text()
                    val=isSymptom(t)
                    if(len(val)>1):
                        f.write(t)

url = "http://symptomchecker.webmd.com/symptoms-a-z"
scraper(url)
