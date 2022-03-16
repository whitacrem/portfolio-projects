# Let's make it a true daily double!

Goal: I want to scrape the score data from every game in the J.Archive website and see how often someone "makes it a true daily double".  This will involved collecting ALL the scores, determining which questions are daily doubles (tagged as class='ddred' in the HTML), then looking at the score before to see if it doubled or fell to 0. Then I also want to know if players are more likely to get the question right when they risk it all... or vice versa.

## March 12

- Learned how to use beautiful soup to write a webscraper
- Iterating through all the game ids, locating the table, and storing info as rows in a dataframe
- Score data is coming back messy - commas, dollar signs, some quote marks? So will need to be cleaned later
- Learned quickly that I need to have question number columns on both ends of my dataframe because the question number is listed on both sides of the scores on J.Archive
- Also learned that some game ids in the loop do not actually have games associated (since the game ids on J.Archive do not just start at 1 and go up as expected), so had to build in a check to make sure beautifulsoup was able to find a table at all
- Added in a print statement in my loop to check for this - because the loop kept unexpectedly crashing and I had to figure out where - and then decided to keep the print statement because it helps me visually track progress

## March 14

- First scraper did not id daily doubles because it was just grabbing all table data, so mimicked the process in a second scraper to find a dataframe of just daily doubles
- Tried a few times to merge the two dataframes so I could id the daily doubles, doing things like making the question number the index, etc
- Realized that the question number keeps repeating so it makes a poor index - there is not a unique game and question id to isolate each individual question. So when merged, the data goes all out of order, which would make it impossible to see what the scores on the question BEFORE the daily double were
- Readjusted original scraper to add the game id as another column in the dataframe it builds
- Readjusted my data processing code to merge the game id and question id to make a unique key for each question and round
- Realized that the scraper was only pulling the data from the first round in each game (single jeopardy)

## March 15
- Changed the "find" to a "find_all" to catch all the tables
- This was catching the final jeopardy tables, which do not have question numbers or daily doubles, so changed the condition in the loop that was checking for more than three players to just check to make sure the data in the row = 5 elements (two question number columns and the scores of three players)
- Added a "round" column to distinguish between jeopardy and double jeopardy, will merge all to make unique IDs for each question