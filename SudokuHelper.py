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
        
        if pg.locateOnScreen('0.png', grayscale=True, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 0

        elif pg.locateOnScreen('1.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 1

        elif pg.locateOnScreen('2.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 2

        elif pg.locateOnScreen('3.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 3

        elif pg.locateOnScreen('4.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 4

        elif pg.locateOnScreen('5.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 5

        elif pg.locateOnScreen('6.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 6

        elif pg.locateOnScreen('7.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 7

        elif pg.locateOnScreen('8.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 8

        elif pg.locateOnScreen('9.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
            sdk[r][c] = 9

        else:
            sdk[r][c] = 0

def tester(r, c, num):
    
    global sdk
    
    for i in range(0,9):
        
        if sdk[r][i] == num:
            return False

    for i in range(0,9):
       
        if sdk[i][x] == num:
            return False
    
    x = (c // 3) * 3
    y = (r // 3) * 3
    
    for i in range(0,3):
      
        for j in range(0,3):
           
            if sdk[y+i][x+j] == num:
                return False

    return True

def helper():
    
    global sdk
   
    for r in range(0,9):
       
        for c in range(0,9):
            
            if sdk[r][c] == 0:
               
                for num in range(1,10):
                    
                    if tester(r, c, num):
                        
                        sdk[r][c] = num
                        helper()
                        sdk[r][c] = 0

                return
      
    print(np.matrix(sdk))
    
    pg.click(390, 260)

    for r in range(0,9):
        
        for c in range(0,9):
            
            pg.press(str(sdk[r][c])) 
            time.sleep(0.25)
            pg.press('right')
            time.sleep(0.25)

        pg.press('down') 
        pg.press('left', presses=8) 

helper()
