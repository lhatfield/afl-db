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
        current = 0
        for a in CurrentUrlArray:
            ScrapeBasicMatchTables(CurrentUrlArray[current])
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


#Magic starts here, get the tables from a match page          
def ScrapeBasicMatchTables(url):
    print('Scraping ' + url)
    print('')
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    #print('asdf')
    tableNo = 0
    count = 0
    teams = []
    #print(soup.prettify())
   
    for a in soup.find_all('a', href=True): #Team Names
        if 'teams' in a['href'] and count < 2:
            teams.append(a.text)
            print(teams[count])
            count = count + 1
           
    for a in soup.find_all('tbody'): #Player Stat lines
        #print(tableNo)
        #print(str(a)[0:200])
        if tableNo == 0 or tableNo == 1:
            ScrapePlayerRow(str(a),teams[tableNo])
            print('=====================================')
        tableNo = tableNo + 1  
   
def ScrapePlayerRow(table, team):
    #Have the two stats tables for all players
    soup = BeautifulSoup(table,'lxml')
    print('==============')
    print('== '+team +' ==')
    print('==============')
    for row in soup.find_all('tr'):
        player = ScrapePlayerData(str(row))
        print(player[1] + ' ' + str(player[2]))
        print('-------------------------------------')
        
def ScrapePlayerData(row): 
     soup = BeautifulSoup(row,'lxml')
     index = 0
     player = []
     for stat in soup.find_all('td'):
         if index == 1 or stat.text.isdigit():
             player.append(stat.text)
         else:
             player.append(0)
         index = index + 1
     return player
               

main();