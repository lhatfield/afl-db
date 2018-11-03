#Script to scrape season information to populate AFL DB
#Created with help from https://youtu.be/ng2o98k983k
#Tutorial starts @ 9.14

from bs4 import BeautifulSoup
import requests
import lxml



def main():
    print('starting')
    ScrapeSeasonsInRange(2018,2018)

#loop through years to be scraped
def ScrapeSeasonsInRange(start,end):
    print('ScrapeSeasons In Range From ' + str(start) + ' to ' + str(end))
    CurrentUrlArray = []
    current = start
    url = 'https://afltables.com/afl/seas/'
    
    #each loop is cycling through a season
    while current <= end:
        #gets all games from given season(at start)
        ScrapeMatchURLFromSeason(url+str(current)+'.html', CurrentUrlArray)
        CurrentUrlArray = CreateURLArray(CurrentUrlArray)
        #for a in CurrentUrlArray:
        ScrapeBasicMatchTables(CurrentUrlArray[0])
        current = current + 1
        
#Format game from Season game page
def CreateURLArray(CurrentUrlArray):
    matchurl = 'https://afltables.com/afl'
    newURLArray = []
    for a in CurrentUrlArray:
        newURLArray.append(matchurl + a[2:100])
    CurrentUrlArray = newURLArray
    return newURLArray
       
#Create an array of URLs for scraping
def ScrapeMatchURLFromSeason(url,CurrentUrlArray): 
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    for a in soup.find_all('a',href=True) :
        if '/stats/games/' in a['href']:
            CurrentUrlArray.append(a['href'])
          
def ScrapeBasicMatchTables(url):
    print('Scraping ' + url)
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    #print('asdf')
    tableNo = 0
    #print(soup.prettify())
    for a in soup.find_all('tbody'):
        tableNo = tableNo + 1
        
       # print(a)
        if tableNo == 1 or tableNo == 2:
            print('Tabel Number ' + str(tableNo))
            ScrapePlayerRow(str(a))
            print('=====================================================================')
     
   
def ScrapePlayerRow(table):
    #Have the two stats tables for all players
    soup = BeautifulSoup(table,'lxml')
    for row in soup.find_all('tr'):
        ScrapePlayerData(str(row))
        print('--------------------------------------------------')

def ScrapePlayerData(row):
     

     soup = BeautifulSoup(row,'lxml')
     index = 0
     print(row)
     print()
     
     for stat in soup.find_all('td'):
         if(index == 0):
             no = stat.text #playernumber
             print(no)
         elif(index == 1):
             na = stat.text #playername
             print(na)
         elif(index == 2): #kicks
             if(stat.text.isdigit()):
                 ki = stat.text
             else:
                 ki = 0
             print(ki)
         elif(index == 3): #marks
             if(stat.text.isdigit()):
                 mk = stat.text
             else:
                 mk = 0
             print(mk)
         elif(index == 4):
             if(stat.text.isdigit()):
                 hb = stat.text
             else:
                 hb = 0
             print(hb)
         elif(index == 5):
             if(stat.text.isdigit()):
                 di = stat.text
             else:
                 di = 0
             print(di)
         elif(index == 6):
             if(stat.text.isdigit()):
                 gl = stat.text
             else:
                 gl = 0
             print(gl)
         elif(index == 7):
             if(stat.text.isdigit()):
                 bh = stat.text
             else:
                 bh = 0
             print(bh)
         elif(index == 8):
             if(stat.text.isdigit()):
                 ho = stat.text
             else:
                 ho = 0
             print(ho)
         elif(index == 9):
             if(stat.text.isdigit()):
                 tk = stat.text
             else:
                 tk = 0
             print(tk)
         elif(index == 10):
             if(stat.text.isdigit()):
                 rb = stat.text
             else:
                 rb = 0
             print(rb)
         elif(index == 11):
             if(stat.text.isdigit()):
                 i50 = stat.text
             else:
                 i50 = 0
             print(i50)
         elif(index == 12):
             if(stat.text.isdigit()):
                 cl = stat.text
             else:
                 cl = 0
             print(cl)
         elif(index == 13):
             if(stat.text.isdigit()):
                 cg = stat.text
             else:
                 cg = 0
             print(cg)
         elif(index == 14):
             if(stat.text.isdigit()):
                 ff = stat.text
             else:
                 ff = 0
             print(ff)
         elif(index == 15):
             if(stat.text.isdigit()):
                 fa = stat.text
             else:
                 fa = 0
             print(fa)
         elif(index == 16):
             if(stat.text.isdigit()):
                 br = stat.text
             else:
                 br = 0
             print(br)
         elif(index == 17):
             if(stat.text.isdigit()):
                 cp = stat.text
             else:
                 cp = 0
             print(cp)
         elif(index == 18):
             if(stat.text.isdigit()):
                 up = stat.text
             else:
                 up = 0
             print(up)
         elif(index == 19):
             if(stat.text.isdigit()):
                 cm = stat.text
             else:
                 cm = 0
             print(cm)
         elif(index == 20):
             if(stat.text.isdigit()):
                 mi = stat.text
             else:
                 mi = 0
             print(mi)
         elif(index == 21):
             if(stat.text.isdigit()):
                 oner = stat.text
             else:
                 oner = 0
             print(oner)
         elif(index == 22):
             if(stat.text.isdigit()):
                 bo = stat.text
             else:
                 bo = 0
             print(bo)
         elif(index == 23):
             if(stat.text.isdigit()):
                 ga = stat.text
             else:
                 ga = 0
             print(ga)
         elif(index == 24):
             if(stat.text.isdigit()):
                 per = stat.text
             else:
                 per = 0
             print(per)
             
         
                
       
         #print(str(playerNumber) + ' ' + playerName)
         index = index + 1
   #      if(index == 0):
   #          playerNumber = stat.text
   #      elif(index == 1): 
   #          playerName = stat.text 
   #      elif(index == 2): 
    #         ki = stat.text 
   #      elif(index ==3 ): 
   #          mk = stat.text

            
    
        

main();