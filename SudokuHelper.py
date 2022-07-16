import numpy as np
import pyautogui as pg
import time

start_time = time.time()

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

        if pg.locateOnScreen('1.png', grayscale=True, confidence=0.9, region=(363+56*c, 238+56*r, size, size)):
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

def tester(row, column, num):
    
    global sdk
    
    for i in range(0,9):
        
        if sdk[row][i] == num:
            return False

    for i in range(0,9):
       
        if sdk[i][column] == num:
            return False
    
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    
    for i in range(0,3):
      
        for j in range(0,3):
           
            if sdk[y0+i][x0+j] == num:
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
            time.sleep(1)
            pg.press('right')
            time.sleep(1)

        pg.press('down') 
        pg.press('left', presses=8) 

helper()

print("Process finished --- %s seconds ---" % (time.time() - start_time))

