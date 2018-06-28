# Artificial Intelligence Tetris Bot

This is a project written in Python for Applied Artificial Intelligence course. It represents AI Bot that can play Tetris and a separate tetris simulation. Object-Oriented programming (OOP) was used while creating the project.

Project was created from scratch following the rules and logic from this site [AI Block Battle](http://theaigames.com/competitions/ai-block-battle/getting-started). Some necceessary parts of the code from the starterbot were used for implementing communication with the engine.


## Communication with the game engine
The communication between the bot and the engine goes via the standard input and output channels. Every single line the engine gives is a specific piece of information or a request. The response from a bot should also be just one line. There are three types of lines, in the following format:

Engine/bot communication works via standard I/O
**Engine -> bot**
Every single line the engine gives is a specific piece of information or a request. There are three types of lines, in the following format:
- `settings [type] [value]` given only at the start of the game. General settings of the game are given here.
- `action [type] [time]` indicates a request for an action.
- `update [player] [type] [value]` this is an update of the game state. `[player]` indicates what bot the update is about, but could also be 'game' to indicate a general update.
**Bot -> engine**
List of moves separated by commas
`left right turnleft turnright down drop no_moves`

File **__test.txt__** shows more clear what the inputs and ouputs look like.


## Heuristics
The main goal of this project was to create a bot that will clear as many lines as possible, and therefore, to make as many moves as possible. To meet this goal, heuristic was used to calculate the best move for a given Tetris piece by trying out all the possible moves (rotation and position). The idea behind the heuristic was followed by this site [Tetris AI – The (Near) Perfect Bot](https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/).


## The best possible move
The score for each move is computed by assessing the grid the move would result in. This assessment is based on four heuristics: aggregate height, complete lines, holes, and bumpiness, each of which the AI will try to either minimize or maximize.
- **Aggregate Height** - this heuristic tells us how “high” a grid is. To compute the aggregate height, we take the sum of the height of each column (the distance from the highest tile in each column to the bottom of the grid). The goal is to minimize this value, because a lower aggreagate heigh means that we can drop more pieces into the grid before hitting the top of the grid.
- **Complete Lines** - the number of complete lines in a grid. The goal is to maximize the number of comlete line becazse clearing lines will give more space for more pieces.
- **Holes** -  a hole is as an empty space such that there is at least one tile in the same column above it. Goal is to minimize holes.
- **Bumpiness** -  the bumpiness of a grid tells the variation of its column heights. It is computed by summing up the absolute differences between all two adjacent columns. The goal is to minimize bumpiness to ensure that the top of the grid is as monotone as possible.

## Simulation
This part was created separately to test the heuristics (aggregate height, complete lines, holes, and bumpiness) before running the AI bot on the website. This simulates a whole game. It keeps track of the state and shows information such as best position for each tetris piece, action moves, score etc. It also keeps track of the averagare number of lines cleared and moves played. 

## How to play a game
Here is are explanation and instructions how to play a game.
- To play a simulation of tetris, run **Test** class.
- To see AI Bot in action , play [demo video](https://www.youtube.com/watch?v=plhzN21yQWg).



