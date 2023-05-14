**_Classes ->_**
1. _**Cell**_
   1. Jump Instance
   2. setter and getter for the jump
2. **_Jump (Snake & ladder)_**
   1. end position
   2. getter for the end position
3. **_Board_**
   1. row_count
   2. cells[][]
   3. jump_mapper
   4. setCells() - To set cell objects into 2-D Array
   5. setJumps() - To add jump objects into the cells
   6. getFinalPosition() - To get the final position after the jump
   7. getBoardSize() - to get the board size
4. **_Game_**
   1. winner
   2. board
   3. dice
   4. players (queue)
   5. initializeGame() -> To initialize board and dice object and add players 
   6. addPlayers() -> To add all Players into Queue
   7. startGame() -> **REAL GAME STARTS THERE VISIT THE LOGIC**
5. **_Dice_**
   1. dice_count
   2. dice_max
   3. roll() -> To get the result of Dice Roll
6. **_Player_**
   1. name
   2. position
   3. getter and setter of the position 
   4. getter of the name

**_Relations_** <br>
**1. Game has a Board<br>**
**2. Game has many Players<br>**
**3. Game has many dices<br>**
**4. Board has many Cells<br>**
**5. Cell has a Jump**


**_Added protection upon cyclic ladder and snake case_**