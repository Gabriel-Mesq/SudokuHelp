import numpy as np
import pyautogui as pg
import time

sdk = [[0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
      
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0]]

size = 56

for r in range(0,9):
    for c in range(0, 9):
        
        if pg.locateOnScreen('numbers\\0.png', grayscale=True, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 0

        if pg.locateOnScreen('numbers\\1.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 1

        elif pg.locateOnScreen('numbers\\2.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 2

        elif pg.locateOnScreen('numbers\\3.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 3

        elif pg.locateOnScreen('numbers\\4.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 4

        elif pg.locateOnScreen('numbers\\5.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 5

        elif pg.locateOnScreen('numbers\\6.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 6

        elif pg.locateOnScreen('numbers\\7.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 7

        elif pg.locateOnScreen('numbers\\8.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 8

        elif pg.locateOnScreen('numbers\\9.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 9

        else:
            sdk[r][c] = 0

def tester(row, column, num):
    
    global sdk
    
    for i in range(0,9):
        
        if sdk[row][i] == num:
            return False

    for i in range(0,9):
       
        if sdk[i][column] == num:
            return False
    
    x = (column // 3) * 3
    y = (row // 3) * 3
    
    for i in range(0,3):
      
        for j in range(0,3):
           
            if sdk[y+i][x+j] == num:
                return False

    return True

def helper():
    
    global sdk
   
    for row in range(0,9):
       
        for column in range(0,9):
            
            if sdk[row][column] == 0:
               
                for num in range(1,10):
                    
                    if tester(row, column, num):
                        
                        sdk[row][column] = num
                        helper()
                        sdk[row][column] = 0

                return
      
    print(np.matrix(sdk))
    
    pg.click(390, 260)

    for r in range(0,9):
        
        for c in range(0,9):
            
            pg.press(str(sdk[r][c])) 
            pg.press('right')
            time.sleep(0.20)

        pg.press('down') 
        pg.press('left', presses=8) 

helper()

