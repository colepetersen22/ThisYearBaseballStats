# ThisYearBaseballStats
Scrapes and prints player statistics from baseball-reference.com

This is my first main attempt at writing a web scraper and integrating more than one language in one project. 
It might be a little messy (especially the Python), but I'm happy with how it turned out.

<h3>ThisYearBaseballStatsUI.java</h3>
Takes inputs for team and stat and prints player stats for that team in the current year. 
Inputs have to match abbreviations used on baseball-reference.com.
This runs StatisticsScraper.py with team, stat, and the current year and reads the updated stats.csv file.

<h3>StatisticsScraper.py</h3>
Takes inputs from ThisYearBaseballStatsUI.java, goes to the current year specified team page at baseball-reference.com, and reads the batting stats table. 
Prints relevant information to stats.csv.
