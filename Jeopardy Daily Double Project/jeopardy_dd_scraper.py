import requests
from bs4 import BeautifulSoup
import pandas as pd

game_id = 1
daily_doubles = []
gameIDs = []
round_list = []

while game_id < 7308:
    URL = "https://www.j-archive.com/showscores.php?game_id="+str(game_id)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    scores_table = soup.find_all("table", {'class':"scores_table"})
    if scores_table:
        round = 1
        for table in scores_table:
            for row in table.find_all('td', {'class':'ddred'}):
                question_number = [i.text for i in row]
                daily_doubles.append(question_number)
                gameIDs.append(game_id)
                round_list.append(round)
            round += 1
    print(str(game_id) + " is done")
    game_id += 1

zipped = list(zip(daily_doubles, gameIDs, round_list))
mydata = pd.DataFrame(zipped, columns=['question', 'gameID', 'round_list'])
mydata.to_csv('dailydoubles.csv')