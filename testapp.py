#!/usr/bin/python

import curses 

window = curses.initscr() 
curses.noecho() 
curses.curs_set(0) 
window.keypad(1) 

window.addstr("This is a Sample Curses Script\n\n") 

while True: 
   event = window.getch() 
   if event == ord("q"): break 
   curr_y, curr_x = window.getyx()
   next_y, next_x = get_next_direction()
   window.move(next_y, next_x)
   window.refresh()
    
curses.endwin()
