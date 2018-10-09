import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN ,init_pair
from random import randint
print("Enter Rows And Columns")
rows,cols=map(int,raw_input().split())
curses.initscr()
curses.start_color()
init_pair(1,curses.COLOR_RED,curses.COLOR_GREEN)
init_pair(2,curses.COLOR_BLUE,curses.COLOR_GREEN)
init_pair(3,curses.COLOR_YELLOW,curses.COLOR_GREEN)
win = curses.newwin(rows, cols, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)
win.bkgd('.',curses.color_pair(3))
key = KEY_RIGHT                                                  # Initializing values
score = 0

snake = [[4,10], [4,9], [4,8],[4,7]]                                     # Initial snake co-ordinates
food = [10,20]                                                     # First food co-ordinates

win.addch(food[0], food[1], '*')                                   # Prints the food

while key != 27:                                                   # While Esc key is not pressed
    win.border(0)
    #win.addstr(0, 2, 'Score : ' + str(score) + ' ')                # Printing 'Score' and
    win.addstr(0, cols/2-4, ' SNAKE ')                                   # 'SNAKE' strings
             
    
    prevKey = key                                                  # Previous key pressed
    event = win.getch()
    key = key if event == -1 else event 


    if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        key = prevKey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
        key = prevKey

    # Calculates the new coordinates of the head of the snake. NOTE: len(snake) increases.
    # This is taken care of later at [1].
    snake.insert(0, [snake[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), snake[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])

    if snake[0][0] == 0: snake[0][0] = rows-2
    if snake[0][1] == 0: snake[0][1] = cols-2
    if snake[0][0] == rows-1: snake[0][0] = 1
    if snake[0][1] == cols-1: snake[0][1] = 1
    #BOundary Conditions

    # If snake runs over itself
    if snake[0] in snake[1:]: break

    
    if snake[0] == food:                                            # When snake eats the food
        food = []
        score += 1
        curses.beep()
        while food == []:
            food = [randint(1, rows-2), randint(1,cols-2)]                 # Calculating next food's coordinates
            if food in snake: food = []
        win.addch(food[0], food[1], '*',curses.color_pair(1))
    else:    
        last = snake.pop()                                          # [1] If it does not eat the food, length decreases
        win.addch(last[0], last[1], ' ')

    win.addch(snake[0][0], snake[0][1], 'o',curses.color_pair(2))

    win.timeout(150 - (len(snake)/2 + len(snake)/5)%120)
    # Increases the speed of Snake as its length increases
win.clear()
win.addstr(rows/2,(cols-18)/2,"Your Score is : "+str(score),curses.color_pair(3))
win.nodelay(0)
x=win.getch()
curses.endwin()
