# Hand Cricket - CLI Game
A simple command-line hand cricket game made with Python. You play against the computer, decide whether to bat or bowl after winning the toss, and try to score more runs than the opponent.

The game also stores match results in a MySQL database, so you can view your previous matches whenever you run the application.
Features
- Head-or-tails toss to decide who gets the choice.
- Choose to bat or bowl when you win the toss.
- Play against the computer using numbers from 1 to 6.
- A matching number ends the batting turn.
- The game calculates the scores and announces the result.
- Saves the toss winner, match winner, scores and date/time in MySQL.
- View saved match history from the menu.
Requirements
- Python 3
- MySQL Server running on your computer
- The MySQL Connector package for Python
Setup
1. Install Python 3 and MySQL Server if they are not already installed.
2. Open a terminal in the project folder.
3. Install the MySQL connector:
   python -m pip install mysql-connector-python
4. Open the Python file and check the MySQL connection details. The current code uses:
   - Host: localhost
   - User: root
   - Password: student
   Change the password in the connection lines if your local MySQL root account uses a different password. .
5. Make sure the MySQL server is running. The program creates the ArshvidFOSS database and the results table automatically the first time it connects.
Menu and commands
The application is menu-driven. Enter one of these choices when prompted:
Menu choice	Action
1 =	Start a new match
2 =	Display saved match history
3 =	Exit the game


During a match:
Prompt      	Input
Toss	        H for Heads or T for Tails
Bat/bowl      choice	B to bat or BO to bowl
Each ball   	A number from 1 to 6


If the player's number matches the computer's randomly selected number, the batting turn ends. Otherwise, the selected number is added to the batting score.
Database
The program creates a database named ArshvidFOSS and a table named results.

The table stores:
- match_id - automatically generated match ID
- toss_winner - who won the toss
- game_winner - who won the match, or Tie
- your_score - player's score
- computer_score - computer's score
- played_at - date and time the record was inserted
