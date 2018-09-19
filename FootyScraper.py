#Script to scrape season information to populate AFL DB
#Created with help from https://youtu.be/ng2o98k983k

from bs4 import BeautifulSoup
import requests
import lxml

def main():
    ScrapeSeasonsInRange(2017,2017)

#loop through years to be scraped
def ScrapeSeasonsInRange(start,end):
    CurrentUrlArray = []
    current = start
    url = 'https://afltables.com/afl/seas/'
    
    #each loop is cycling through a season
    while current <= end:
        #gets all games from given season(at start)
        ScrapeMatchURLFromSeason(url+str(current)+'.html',CurrentUrlArray)
        FormatBasicUrltoComplete(CurrentUrlArray)
        
#Format game         
def FormatBasicUrltoComplete(CurrentUrlArray):
    matchurl = 'https://afltables.com/afl'
    for a in CurrentUrlArray:
        a = matchurl + a[2:100]
        print('formatting '+ a)
       
#Create an array of URLs for scraping
def ScrapeMatchURLFromSeason(url,CurrentUrlArray): 
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    for a in soup.find_all('a',href=True) :
        if '/stats/games/' in a['href']:
            CurrentUrlArray.append(a['href'])


def ScrapebasicMatchTables(url):
    source = requests.get(url).text
    soup = BeautifulSoup(source,'l xml')
    ScrapeTeamStats(soup.find('sortableTable0'))
    ScrapeTeamStats(soup.find('sortableTable1'))
    #Get scoring progression here
    
def ScrapeTeamStats(team):
    for player in team.find_all('div',class_='tr'):
        ScrapePlayerRow(player)
    
def ScrapePlayerRow(player):
    stats = []
    #append the player page to the stat line
    stats[0] = player.find('a',href=True)
    for stat in player.find_all('div',class_='td'):
        if len(stat) > 0:
            stats.append(stat)
        else:
            stats.append(0) #AFL Tables if they did not record a stat there is no 0
            
    PlayerID = PlayerInDB(stats[1])
    if PlayerID == -1:
         #create new entry for player
         
    #Insert array data into database            
    
    
def PlayerInDB(stats): #return id
    
    playername = stats[0]
    
    return 69

    
  
