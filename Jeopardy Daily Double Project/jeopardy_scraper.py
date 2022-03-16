import requests
from bs4 import BeautifulSoup
import pandas as pd

# Establish a game_id variable so I can run a loop.  As of Mar 12 2022, the game ids on J.archive run up to 7307.
game_id = 1

# Establish an empty dataframe to store data.
mydata = pd.DataFrame(columns=['question', 'contestant1', 'contestant2', 'contestant3', 'question2', 'gameID', 'round'])

# Loop through all possible game ids (up to Mar 12, not including national college championship)
while game_id < 7308:
    URL = "https://www.j-archive.com/showscores.php?game_id="+str(game_id)
    page = requests.get(URL)

    # Save game ID as a list so it can be added to df later
    gameID = [game_id]

    soup = BeautifulSoup(page.content, "html.parser")
    scores_table = soup.find_all("table", {'class':"scores_table"})
    # Check to see if the scores table actually exists
    if scores_table:
        round = [1]
        for table in scores_table:
            for row in table.find_all('tr')[1:]:
                row_data = row.find_all('td')

                # Check to make sure there were only three players in the game - some special games with 4+ players were breaking the loop
                if len(row_data) != 5:
                    break
                else:
                    row = [i.text for i in row_data] + gameID + round
                    length = len(mydata)
                    mydata.loc[length] = row
            round[0] += 1
    print(str(game_id) + " is done")
    game_id += 1

mydata.to_csv('jeopardy_scores.csv')

