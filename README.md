[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12803446&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Stars 
## CS110 Final Project   Fall, 2023 

## Team Members
Melis Atagun
Mehmet Akarca

## Project Description
We will create 2048 game for final project. First, we will design an interface featuring a game board with a matrix to hold the numbers. Then, we will design a controller to manage player movements(right, left, up, down). The game is played on a 4x4 board, and the goal is to achieve the number 2048 by combining tiles that are multiples of 2

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start screen 
2. User input for swiping  
3. Tile adding logic 
4. Move availability check 
5. Game over screen 

### Classes
GameController
GameBoardView
BoxView 
GameBoard 
Box

## ATP

Test Case 1: Menu Navigation and Game Start

Test Description: Verify that the game menu functions are correct and that game start and end functionalities work as expected.
Test Steps:
Start the game.
Press the 'S' key to start the game.
Press the 'Q' key to end the game.
Verify that there are only two tiles on the board when the game starts.
Expected Outcome: Pressing 'S' should start the game, and pressing 'Q' should end the game. At the start of the game, there should only be two tiles on the board.

Test Case 2: Tile Movement and Merging

Test Description: Ensure that tiles move as expected in terms of arrow key inputs and that matching neighbor numbers merge correctly.
Test Steps:
Start the game.
Use the arrow keys (down, up, right, left) to move the tiles.
Check if matching numbers merge.
Expected Outcome: Tiles should move in the direction of the pressed arrow key and matching numbers should merge to form their sum.

Test Case 3: Adding New Tiles

Test Description: Confirm that a new tile is added to the board after each valid move.
Test Steps:
Start the game and make a few moves.
After each move, check if a new tile appears on the board.
Expected Outcome: A new tile (either 2 or 4) should be added to a random empty cell after each valid move.

Test Case 4: Game Over Condition

Test Description: Confirm the game ends correctly when no more moves are possible.
Test Steps:
Play the game until the board is full.
Check if the "Game Over" message appears when the board is full and no more matching tiles to merge.
Expected Outcome: The game should display a "Game Over" message and end when the board is full and no more moves can be made.

Test Case 5: High Score Tracking
Test Description: Ensure the game correctly records and displays the high score.
Test Steps:
Start the Game: Open the game.
Achieve a Score: Play the game and note the score achieved.
End the Game: Finish the game session.
Restart the Game: Close and reopen the game.
Check High Score: Observe if the previous high score is displayed.
Expected Outcome: The high score achieved in the first game session should be displayed when the game is restarted. The high score remains the same unless a new high score is achieved.
