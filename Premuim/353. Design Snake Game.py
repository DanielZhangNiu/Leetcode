"""
 Design a Snake game that is played on a device with screen size = width x height. Play the game online if you are not familiar with the game.

 The snake is initially positioned at the top left corner (0,0) with length = 1 unit.

 You are given a list of food's positions in row-column order. When a snake eats the food, its length and the game's score both increase by 1.

 Each food appears one by one on the screen. For example, the second food will not appear until the first food was eaten by the snake.

 When a food does appear on the screen, it is guaranteed that it will not appear on a block occupied by the snake.

 Example:

 Given width = 3, height = 2, and food = [[1,2],[0,1]].

 Snake snake = new Snake(width, height, food);

 Initially the snake appears at position (0,0) and the food at (1,2).

 |S| | |
 | | |F|

 snake.move("R"); -> Returns 0

 | |S| |
 | | |F|

 snake.move("D"); -> Returns 0

 | | | |
 | |S|F|

 snake.move("R"); -> Returns 1 (Snake eats the first food and right after that, the second food appears at (0,1) )

 | |F| |
 | |S|S|

 snake.move("U"); -> Returns 1

 | |F|S|
 | | |S|

 snake.move("L"); -> Returns 2 (Snake eats the second food)

 | |S|S|
 | | |S|

 snake.move("U"); -> Returns -1 (Game over because snake collides with border)
"""
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        initial_pos = (0, 0)
        self.snake = collections.deque([initial_pos])
        self.snakebody = set([initial_pos])
        self.foods = food
        self.width, self.height = width, height
        self.directions = { 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0) }
        
    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """
        head = self.snake[0]
        move = self.directions[direction]
        next_pos = (head[0] + move[0], head[1] + move[1])
        
        # Remove the tail before checking because the new head
        # can be in the previous tail position.
        tail = self.snake.pop()
        self.snakebody.remove(tail)
        if next_pos[0] < 0 or next_pos[0] >= self.height or next_pos[1] < 0 or next_pos[1] >= self.width or next_pos in self.snakebody:
            return -1
        
        # Add next position into snake's head
        self.snake.appendleft(next_pos)
        self.snakebody.add(next_pos)
        
        # Considerate the food issue, extend snake
        curr_food = (-1, -1)
        if self.foods:
            curr_food = tuple(self.foods[0])
        
        if curr_food == next_pos:
            self.foods.pop(0)
            # Add back tail because eating the food is
            # equivalent to combining the food with the body.
            self.snake.append(tail)
            self.snakebody.add(tail)

        # Score is proportional to snake length.
        return len(self.snakebody) - 1
        
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
