import numpy as np
f = open("predModel.csv","w")
f.write("volt,temp1,temp2,vibration,speed,lubricant,power failure,temp1 failure,temp2 failure,extreme vibration,speed error,lubricant required,days left")
def gen(volt_input:int,
        temp1:float,
        temp2:float,
        freq:int,
        speed:int,
        lbc:int):
    min_date = 10000
    err_type = [0,0,0,0,0,0]
    #voltage error calculator
    if volt_input > (max_v := 511) or volt_input < (min_v := 394):
        days_left = max(30 - ((volt_input - max_v) if volt_input > max_v else (min_v - volt_input)),0)
        if days_left < min_date:
            err_type = [1,0,0,0,0,0]
            min_date = days_left
    # tempreture 1
    if temp1 > 75:
        days_left = 30 - round(min((temp1 - 75)/1.933,30))
        if days_left < min_date:
            err_type = [0,1,0,0,0,0]
            min_date = days_left
    # tempreture 2
    if temp2 > 55:
        days_left = 30 - round(min((temp2 - 55)/2,30))
        if days_left < min_date:
            err_type = [0,0,1,0,0,0]
            min_date = min(min_date,days_left)
    #vibration
    if freq > 600:
        days_left = round((freq-500)/17.46) if round((freq-500)/17.46) < 30 else 30
        if days_left < min_date:
            min_date = days_left
            err_type = [0,0,0,1,0,0]    
    # speed
    if not (speed in range(27,54)):
        if speed < 27:
            days_left = abs(round(30-(27-speed)*1.3))
        else:
            days_left = abs(round(30 - (speed - 54)*1.3))
        if days_left < min_date:
            err_type = [0,0,0,0,1,0]
            min_date = days_left
        
    # lubricant
    if lbc > 10:
        days_left = (33 - lbc)
        if days_left < min_date:
            min_date = days_left
            err_type = [0,0,0,0,0,1]
    if not any(err_type):
        return (err_type,-1)
    return (err_type, min_date)
w = open("predModel.csv","a")
for i in range(5000):
    print('----------------------------intreation:',i+1)
    '''if i%10 == 0:
        c = 0
        print(c)
        while c < 1:
            volt = np.random.randint(370,530)
            temp1 = np.random.uniform(40,95)
            temp2 = np.random.uniform(30,70)
            frequency = np.random.randint(300,900)
            speed = np.random.randint(19,60)
            lubricant = np.random.randint(0,15)
            inputs = [volt,temp1,temp2,frequency,speed,lubricant]
            if (ip:=gen(volt,temp1,temp2,frequency,speed,lubricant))[-1] == -1:
                print(str(inputs + ip[0]+[ip[-1]])[1:-1])
                w.write("\n"+str(inputs + ip[0]+[ip[-1]])[1:-1])
                
                c+=1'''
    

    volt = np.random.randint(370,530)
    temp1 = np.random.uniform(40,95)
    temp2 = np.random.uniform(30,70)
    frequency = np.random.randint(300,900)
    speed = np.random.randint(19,60)
    lubricant = np.random.randint(0,15)
    inputs = [volt,temp1,temp2,frequency,speed,lubricant]
    
    x = inputs + (s:=gen(volt,temp1,temp2,frequency,speed,lubricant))[0] + [s[1]]

    dataline = str(x)[1:-1]
    print(dataline)
    w.write("\n"+dataline)