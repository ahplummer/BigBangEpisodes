from bs4 import BeautifulSoup
import requests
import string
import json

class Episode(object):
    def __init__(self, episodeName, airDate, episodeNumber, seriesInfo):
        self.EpisodeName = episodeName
        self.AirDate = airDate
        self.EpisodeNumber = int(episodeNumber)
        self.SeriesInfo = seriesInfo
    def __str__(self):
        return "Season {}, Episode Number {}, entitled {}, aired on {}".format(
            self.SeriesInfo, self.EpisodeNumber, self.EpisodeName, self.AirDate)

def ScrapeData():
    Episodes = []
    url = "https://bigbangtheory.fandom.com/wiki/List_of_The_Big_Bang_Theory_episodes"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, features="html.parser")
    tables = soup.find_all("table", attrs={"class": "wikitable"})
    h2s = soup.find_all("span", attrs={"class": "mw-headline"})
    h2Index = 1
    for table in tables:
        table_rows = table.tbody.find_all("tr")  # contains 2 rows
        for tr in table_rows:
            table_elements = tr.find_all("td")
            if len(table_elements) == 3:
                title = table_elements[0].text.strip()
                title = ''.join(filter(lambda x: x in string.printable, title))
                airdate = table_elements[1].text.strip()
                episodeNumber = table_elements[2].text.strip()
                seasonInfo = h2s[h2Index].text
                ep = Episode(title, airdate, episodeNumber, seasonInfo)
                Episodes.append(ep)
        h2Index += 1
    return Episodes

def BuildJson(episodes):
    wholelist = []
    for ep in episodes:
        epdict = dict()
        epdict["Season"] = ep.SeriesInfo.replace("\u2013", "-")
        epdict["Title"] = ep.EpisodeName
        epdict["Episode"] = ep.EpisodeNumber
        epdict["FirstAired"] = ep.AirDate
        wholelist.append(epdict)
    wholedict = dict()
    wholedict["Episodes"] = wholelist
    return wholedict

if __name__ == "__main__":
    eps = ScrapeData()
    mydict = BuildJson(eps)
    myjson = json.dumps(mydict, indent=5)
    print(myjson)