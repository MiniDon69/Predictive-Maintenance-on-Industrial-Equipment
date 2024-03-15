import numpy as np
def gen(temp1:float):
#def generate_output(volt_input,temp1,temp2,motion,vibration,lubricant,last_maintainance_type,last_maintance_date):
    error_types = []
    min_date = 31
    #voltage error calculator
    if temp1 > 75:
        days_left = 30 - round(min((temp1 - 75)*1.933,30))
        min_date = min(min_date,days_left)
        return ("voltage error",round(days_left))
    #temp1 error calculator
    #if temp1 > 78.8
for i in range(100):
    if i % 10 == 0:
        
    v = np.random.uniform(60,100)
    print("volt:",v,"error type:",gen(v))