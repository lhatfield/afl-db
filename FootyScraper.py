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
            print('Team Number ' + str(tableNo))
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
     player = []
   
     
     for stat in soup.find_all('td'):
         if index == 1 or not stat.text.isdigit():
             player.append(stat.text)
         else:
             player.append(0)
         index = index + 1
     print(player[1])
          
        
  
    
     #print('Kicks ' + str(ki)+ ', Handballs ' + str(hb) + ', Disposals ' + str(di))
         
      



        

main();