# A baseball-reference.com scraper that takes inputs of team and stat and outputs current year results to stats.csv

__author__ = "Cole Petersen"

import sys
import requests
import csv
from bs4 import BeautifulSoup

# get inputs
team = sys.argv[1]
stat = sys.argv[2]
year = sys.argv[3]

# go to current year page for the specified team
url = "http://www.baseball-reference.com/teams/" + team + "/" + year + ".shtml"
r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

data = soup.find_all("table", {"id": "team_batting"})  # find the batting statistics table

p = []
s = []
statlist = []
ps = []
printstring = ""

for d in data:
    size = len(d.contents[6].find_all("tr", class_=lambda y: y != 'thead'))
    for x in range (0, size):

        # get all players who have at least one of the stat
        if d.contents[6].find_all("td", {"data-stat": stat})[x].text != "":
            if int(d.contents[6].find_all("td", {"data-stat": stat})[x].text) > 0:
                # add the player and stat value to their respective lists
                p.append(str(d.contents[6].find_all("td", {"data-stat": "player"})[x].text))
                s.append(str(d.contents[6].find_all("td", {"data-stat": stat})[x].text))

size = len(p)

# add each pair of player and stat value to another list
for x in range (0, size):
    statlist.append([p[x], s[x]])

# sort the list
sort = sorted(statlist, key=lambda y: int(y[1]))
sort.reverse()

# set up string for each player and remove extra characters
for x in range(0, size):
    printstring = ': '.join(sort[x])
    printstring = printstring.replace("*", "")
    printstring = printstring.replace("#", "")
    printstring = printstring.replace("?", "")
    ps.append(printstring)

# write each string to stats.csv
with open("src\\ThisYearBaseballStats\\stats.csv", 'w+') as f:
    writer = csv.writer(f)
    for a in ps:
        writer.writerow([a])
