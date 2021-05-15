







# Snake Game, Jared Wogan
# Version 1.0
# May 14, 2020

import random
import curses
import os

cmd = 'mode 50,20'
os.system(cmd)

screen = curses.initscr()
curses.curs_set(0)
screen_h, screen_w = screen.getmaxyx()
# print(sh,sw)
window = curses.newwin(screen_h, screen_w, 0, 0)
window.keypad(1)
window.timeout(100)

snake_x = int(screen_w/4)
snake_y = int(screen_h/2)
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x-1],
    [snake_y, snake_x-2]
]

food = [int(screen_h/2), int(screen_w/2)]
window.addch(int(food[0]), int(food[1]), curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    # print('Food:',food)
    # print('Snake Head:',snake[0])
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, screen_h] or snake[0][1]  in [0, screen_w] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, screen_h-1),
                random.randint(1, screen_w-1)
            ]
            food = new_food if new_food not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(int(tail[0]), int(tail[1]), ' ')

    window.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)
