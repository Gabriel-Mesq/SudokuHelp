import numpy as np

sdk = [[0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
      
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0],
       [0,0,0, 0,0,0, 0,0,0]]

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
    input('More possible solutions')

helper()
