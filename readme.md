# SDPA Coursework (01/23)

## Dots and Boxes

### Introduction

Dots and Boxes is a pencil and paper game for two players, where the goal is to complete the most boxes (and thus gain the most points). To do this, players draw one line per turn, with points awarded to the current player when a box is completed. In this implementation, there are two players (A & B) who battle it out over the command line. Player A must be a human, although player B can be either human or computerised. The computer can play using one of two approaches: Random or Smart.

There are two ways to play the game:

- via `Board.initialise()` - The game starts by bringing up an options menu, allowing you to select player types, board size, helper functions and debug options
- via `Board.play()` - Starts without the options menu, requires a board set up with players. Useful for debugging specific scenarios

In the options menu, it is possible to enable _Show Possible moves and ratings_. For each human player this gives a list of the best moves according to the computer. Whilst primarly designed for debugging the smart player, I find it useful for identifying strategies.

### Player types

#### Human

- A human interacts with the game via the command line
- Human players are asked to enter coordinates in the form `x1,y1,x2,y2`
  - Axes are inverted Y, standard X

#### Random

- The computer draws valid lines at random

#### Smart

- The computer calculates the best moves, and selects the one that can gain it the most points.

### File structure

All files for the game are located in the `./game/` folder

#### `main.py`

- Entry point
- This file contains the initalisation and required imports for the game.

#### `classes/Board.py`

- `Board` class
  - All of the routines and features associated with the board or game overall
  - Initialisation and game loop

#### `classes/Player.py`

- `Player` class
  - Attributes associated with players
- `Random` class
  - Child of `Player`
  - Contains the inputs for the random computer player
- `Human` class
  - Child of `Player`
  - Contains the inputs for the human computer player
- `Smart` class
  - Child of `Player`
  - Contains the inputs for the smart computer player

#### `classes/Move.py`

- `Move` class
  - Responsible for rating moves for the smart computer player

### Design decisions

When originally designing the board I chose to take a inverted Y axis primarily because this makes drawing easier - it is the order that drawing occurs in. This is not entirely ideal for players who are used to standard XY grids, but I don't think it adds too much complexity, and is quite clearly shown on the board.

Another area that caused quite a lot of headaches was rating a move. I originally tended towards allowing simultaneous entry, but ended up removing this as an option due to time constraints. Finding a way of rating moves with foresight in such a way that the other player couldn't beat you immediately was challenging, but I ended up with +3 for a line that completes a box this turn, and +1 for one that completes a box in 2 turns time - this provides a balance, and keeps the obvious blocking moves away.

In keeping with the _don't repeat yourself_ philosophy, almost every duplicate instance is abstracted to a function. A key example of this is settings - the entry and validation is handled by a seporate function called by the initialisation routine.

Finally, there are a number of time delays added, during initalisation and when computer players are determining moves. I think that this makes it feel much more like you are playing an actual game against a player, similar to an animation or cutscene. It also improves clarity as you clearly see the move and when it becomes your turn. Unfortunately due to limitations of how pure python handles inputs, this means that if you type anything during one of these pauses it is taken as an input when the program resumes, which can result in one or two lines of invalid input. This could be resolved by using a library (e.g. Delay), but that is outside of the scope of this project.

## Data Analytics

Content for part 2 can be found in `./dataAnalytics/index.ipynb`

The project is dependent on:

- spotipy - Spotify API library
- numpy
- pandas
- seaborn
