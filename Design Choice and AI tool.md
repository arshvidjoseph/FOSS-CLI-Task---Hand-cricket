# Design Notes.
## Project idea
A terminal-based hand cricket game where a player competes against a computer opponent. The application also keeps a history of completed matches using MySQL.
### Design choices
- Command-line interface: Keeps the game straightforward and focuses on Python fundamentals, input, loops, conditions and functions.
- Random number generation: Python's random module is used for the toss and the computer's number.
- Menu: The three menu options make it easy to start a match, check earlier results or exit.
- MySQL storage: Match information is stored in a database instead of disappearing when the program closes.
- Separate functions: startgame(), score(), view_score() and menu() divide the main tasks into smaller sections.
# AI tools
No AI tools were used for creating the CLI project
