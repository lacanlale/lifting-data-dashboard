import pandas as pd
import time
import random

# Goal
# ----
# Generate a dataset of excercise movements, the weight lifted, sets and reps for that day, and the RPE
# Example:
# Date | Day Type | Movement | Movement Type | Weight | Sets | Reps | RPE
# -------------------------------------------------------------
# 06-23-2021 | Legs | Squat | Compound | 225 | 1 | 8 | 9
# 06-22-2021 | Pull | Cable Curls | Isolation | 70 | 3 | 10 | 8
# ... | ... | ... | ... | ... | ... | ... | ... 
# 
# Notes:
#   - There are two main types of movements: Compound and Isolation
#   - RPE will be between 7-10 (since it's unrealistic to be counting anything below in training)
#   - Dates will be formatted as MM-DD-YYYY
#   - Day type will either be Push, Pull, or Legs
#   - The data generated here is a bit nonsensical and only has compound movements. The columns here are simply to represent
#     the acutal dataset


def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))
 
 
def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


compounds = [
        ('Push','Bench Press'),
        ('Pull','Deadlift'),
        ('Legs','Back Squat'),
        ('Push','OHP'),
        ('Pull','Barbell Row'),
        ('Legs','Front Squat')
        ]

data = {'Date' : [],
        'Day Type' : [],
        'Movement' : [],
        'Movement Type' : [],
        'Weight' : [],
        'Sets' : [],
        'Reps' : [],
        'RPE' : []}

for _ in range(0,1000):
    data['Date'].append(random_date("1/1/2021", "12/31/2021", random.random()))
    movement = compounds[random.randint(0,len(compounds)-1)]
    data['Day Type'].append(movement[0])
    data['Movement'].append(movement[1])
    data['Movement Type'].append('Compound')
    data['Weight'].append(random.randrange(135,405,5))
    data['Sets'].append(random.randint(1,5))
    data['Reps'].append(random.randint(1,10))
    data['RPE'].append(random.randint(7,10))
    
df = pd.DataFrame(data)
df.sort_values(by='Date', axis=0, inplace=True)
df.to_csv('data/dummy_data.csv', index=False)
