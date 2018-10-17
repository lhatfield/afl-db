#Script to scrape season information to populate AFL DB
#Created with help from https://youtu.be/ng2o98k983k

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
    tables = soup.find_all('table')
    print('asdf')
    for a in tables:
        print('herio')
        print(str(a.prettify))
        print('-----------------------------------------------')
    #home = tables[4].find('tbody')
    #ScrapeTeamStats(home)
    #away = tables[2].find('tbody')
    #ScrapeTeamStats(away)
    
   # scoring = tables[6].text
  
     
def ScrapeTeamStats(team):
    soup = BeautifulSoup(team, 'lxml')
    print('team' + team)
    print(' ')
    print(' ')
    print('------------------------------------------------------------------ ')
    for player in soup.find_all('tr'):#add player URL
        print('player ' + player) 
        #ScrapePlayerRow(player)
    
def ScrapePlayerRow(player):
    stats = []
    #append the player page to the stat line
    stats[0] = player.find('a',href=True)
    for stat in player.find_all('div',class_='td'):
        if len(stat) > 0:
            stats.append(stat)
        else:
            stats.append(0) #AFL Tables if they did not record a stat there is no 0
    #PlayerID = PlayerInDB(playerURL)
   # if PlayerID == -1:
     #   player[0]
         #create new entry for player
         
         
    #Insert array data into database            
    
def CreateNewPlayerEntry(playerName, DOB):
    #connect to database/ check connection
    #player ID auto increments
    #Name, DOB, Height, Weight, Armspan
    newPlayerQuery = 'INSERT INTO Player VALUES'+ playerName + ' ' + DOB
    findPlayerId = 'SELECT playerID from Player WHERE playerName === ' + playerName + ' AND DOB === ' + DOB
    
    #exec queries
    playerID = 123
    return playerID
    

def PlayerInDB(playerURL): #return id
    #create request for player information
    #get name and DOB, limitation, if two players have the ame name and were born on the same day
    playerName = '<name>'
    DOB = '<xx/yy/zzzz>'
    #Query to database to find 
    query = 'SELECT playerID FROM PLAYER WHERE name ===' + player + ' AND DOB ===' + DOB
    #exec query
    query = 0
    if query < 0: #if err/ not found
       query = CreateNewPlayerEntry(playerName, DOB)
    return query


def ScrapeMatchInfo(MatchTable):
    soup = BeautifulSoup(MatchTable, 'lxml')
    information = soup.findall('td')[1]
    print(information)
    
    #roundNum = information.split[1,1]
    #ground = 0
    #attendance= 0
    #date= 0
    
main();
