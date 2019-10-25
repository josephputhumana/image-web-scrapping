import os
import urllib.request as ulib 
from bs4 import BeautifulSoup as Soup 
import ast 
from selenium import webdriver
 
chromePath=r'C:\Users\joseph\Documents\Web Scrapping\chromedriver.exe'
driver = webdriver.Chrome(chromePath)

URL='https://www.google.com/search?rlz=1C1CHBF_enIN864IN864&biw=767&bih=744&tbm=isch&sxsrf=ACYBGNSISqZ_CG9SIVLtB5i4RjD8e1FxtA%3A1571939889864&sa=1&ei=MeaxXequNOLC3LUP9dSlkA0&q=cat+photos&oq=cat+photos&gs_l=img.1.0.0i67j0l3j0i67j0l5.9651279.9653147..9657199...0.0..0.198.579.0j4......0....1..gws-wiz-img.......0i7i30.rHv290O53MY'

def getURls(URL):
    driver.get(URL)
    a=input()
    page=driver.page_source
    #print(page)
    
    soup=Soup(page)
    desiredURLs=soup.findAll('div',{'class':'rg_meta notranslate'})
    ourURLs=[]
    for url in desiredURLs:
        theURL=url.text 
        #print(theURL)
        theURL=ast.literal_eval(theURL)['ou']
        ourURLs.append(theURL)
    return(ourURLs)    

directory='cats'
def save_images(URLs,directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i,url in enumerate(URLs):
        savePath=os.path.join(directory,'{:06}.jpg'.format(i))

        try:
            ulib.urlretrieve(url,savePath)
        except:
            print("failed",url)




URLs=getURls(URL)
#for url in URLs:
    #print(url)

save_images(URLs,directory)