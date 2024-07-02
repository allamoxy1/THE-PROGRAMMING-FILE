 # importing the time module  
import time  
# defining the countdown function.  
def countdown(c):      
    while c:  
        m, s = divmod(c, 60)  
        timer = '{:02d}:{:02d}'.format(m, s)  
        print(timer, end="\r")  
        time.sleep(1)  
        c -= 1       
    print('time up ya m3alem sha2lasha')  # input the time value in seconds  
c = input("Enter the time value in seconds: ")  
# function call at the program  
countdown(int(c))  