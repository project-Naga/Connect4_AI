# ConnectFour

ConnectFour is a classic game implemented in Python, featuring AI players and a GUI for interactive gameplay.

## Files

- `ConnectFour.py`: Contains the game logic and GUI functions.
- `Player.py`: Defines different types of players:
  - `AIPlayer`: Implements AI algorithms for making moves.
  - `RandomPlayer`: Chooses moves randomly.
  - `HumanPlayer`: Allows human input for moves.

### GUI Description
![img1.png](imgaes/img1.png)

- The top text displays the player making the next move.
- Circles represent the game board.
- The "Next Move" button progresses the game.
- Upon game end, the top text displays the winning player.

## Usage

- To play the game, run the following command:
  - "python ConnectFour.py arg1 arg2"

- arg1 and arg2 can be AI, random, or human.
- For example, to play against a random player: python ConnectFour.py human random.
- To let AI players play against each other: python ConnectFour.py ai ai.

Shown below is an example of a Random player:
![img2.png](imgaes/img2.png)
  
### AI Algorithms
- get_alpha_beta_move(board): Implements Alpha-Beta Pruning.
- get_expectimax_move(board): Implements the Expectimax algorithm.
- evaluation_value(board): Provides evaluation values for game states.
  
### Game Tree Exploration
- Due to the complexity of exploring the entire game tree, depth-limited search is used, initially set to a depth of 5.
- You can modify the depth if required.


