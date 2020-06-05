import numpy as np
import math
import time as tm
total = np.zeros(8)
time = np.zeros(8)
rate = np.array([20,12,8])
dept = np.array([60,54,43])
new_car = np.zeros(8)
old_car = np.zeros(8)
x = ["red" for i in range(8)]
light_stat = np.array(x)
def time_cal(total):
    for i in range(0,4):
        if total[i] > 140:
            time[i] = math.ceil(total[i]/25 )           
        elif total[i] > 70:
            time[i] = math.ceil(total[i]/20 )  
        elif total[i]==0:
            time[i]=0      
        else:
            time[i] = math.ceil(total[i]/15 )
for i in range(0,4):
     total[i] = int(input("Enter initial no of vehicle in " + str(i) + " light: "))

time_cal(total)
print(time)
old_car = total.copy()
new_car=total.copy()
print(old_car)
print(new_car)


active=time.argmax()



def time_dec(active):
        time[active] -= 1
    

def car_dec(active):
    if total[i] > 140:
        new_car[active]=new_car[active]-25 
        if new_car[active]<0:
            new_car[active]=0    
    elif total[i] > 70:
        new_car[active]=new_car[active]-20 
        if new_car[active]<0:
            new_car[active]=0               
    else:
        new_car[active]=new_car[active]-15
        if new_car[active]<0:
            new_car[active]=0   

def light_status(active):
    light_stat[active] = "green"
    print("\nLight " + str(active) + " is green for " + str(time[active]) + "seconds", end="\n")
   

def light_operation(active):
    while time[active]>0:
        light_status(active)
        car_dec(active)
        time_dec(active)
        print("\r" + "Time Left: "+ str(time[active]) + " Old Cars Left: "+ str(new_car[active]), end = "")
        tm.sleep(1)
        print("\n All Other Traffic Lights are Red!\n")
    
for j in range(0,4):
    for i in range(0,4):
        light_operation(active)
    time1=time[time<=time.max()]
    active=time1.argmax()
    
    










    

    
   
    
    


        
    

